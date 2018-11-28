#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
	string mas[105];
	double wp[105], owp[105], oowp[105];
	int kols[105];
	memset(kols, 0, sizeof(kols));
	ifstream inf("input.txt");
	int n;
	int t;
	inf >> t;
	FILE* f = fopen("output.txt", "w");
	for (int tt = 0; tt < t; tt++) {
		inf >> n;
		for (int i = 0; i<n; i++)
			inf >> mas[i];
		for (int i = 0; i < n; i++) {
			int sum = 0 , kol = 0;
			for (int j = 0; j < n; j++)
				if (mas[i][j]=='1') {
					sum++;
					kol++;
				} else if (mas[i][j]=='0')
					kol++;
			if (kol != 0)
				wp[i] = double(sum)/kol;
			else
				wp[i] = 0;
			kols[i] = kol;
		}
		for (int i = 0; i<n; i++) {
			int kol = 0;
			double sum = 0;
			for (int j = 0; j<n; j++)
				if (mas[i][j] == '1') {
					if (kols[j] != 1)
						sum += wp[j]*kols[j]/double(kols[j]-1);
				} else if (mas[i][j] == '0') {
					if (kols[j] != 1)
						sum += (wp[j]*kols[j]-1)/double(kols[j]-1);
				}
			if (kols[i] != 0)
				owp[i] = sum / kols[i];
			else
				owp[i] = 0;
		}
		for (int i = 0; i<n; i++) {
			double sum = 0;
			for (int j = 0; j<n; j++)
				if (mas[i][j]!='.')
					sum += owp[j];
			if (kols[i]!= 0)
				oowp[i] = sum/kols[i];
			else
				oowp[i] = 0;
		}
		for (int i = 0; i<n; i++)
			printf("%0.10f\n", wp[i]);
		for (int i = 0; i<n; i++)
			printf("%0.10f\n", owp[i]);
		for (int i = 0; i<n; i++)
			printf("%0.10f\n", oowp[i]);
		
		
		
		fprintf(f,"Case #%d:\n", tt+1);
		
		for (int i = 0; i<n; i++)
			fprintf(f,"%0.10f\n", 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);


	
	}
	fclose(f);
	return 0;
}