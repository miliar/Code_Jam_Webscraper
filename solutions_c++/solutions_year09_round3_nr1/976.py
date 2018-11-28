

#include <iostream>
#include <fstream>

using namespace std;

int main()
{
//	FILE* fp1 = freopen("A-small-attemp0.in", "r", stdin);
//	FILE* fp2 = freopen("a.out", "w", stdout);

	ifstream ipfile("A-small-attempt2.in", ios_base::in);
	ofstream opfile("a.out", ios_base::out);
	int T;
	ipfile >> T;
	for(int i = 1; i <= T; i++)
	{
		char str[1024];
		ipfile >> str;
		
		int base = 0;
		char buf[256];
		memset(buf, 0, 256);
		for(int j = 0; j < strlen(str); j++)
			buf[str[j]] = 1;
		
		for(int j = 0; j < 256; j++)
		{
			if(buf[j]) base++;
		}
		
		int* arr = new int[strlen(str)];
		for(int j = 0; j < strlen(str);j ++)
		{
			arr[j] = 0;
		}
		int val = 1;
		for(int j = 0; j < strlen(str); j++)
		{
			if(arr[j]) continue;
			arr[j] = val;
			int k = j;
			while(k < strlen(str))
			{
				if(str[j] == str[k]) arr[k] = val;
				k++;
			}
			val++;
		}
		
		for(int j = 0; j < strlen(str); j++)
		{
			if(arr[j] == 2) arr[j] = 0;
			else if(arr[j] != 1) arr[j]--;
		}
		unsigned long long ans = 0;
		
		if(base == 1) base = 2;
		int baseP = 1;
		for(int j = strlen(str)-1; j >= 0; j--)
		{
			ans += arr[j]*baseP;
			baseP *= base;
		}
		
		opfile << "Case #" << i << ": " << ans << endl;
	}
	ipfile.close();
	opfile.close();
//	fclose(fp1);
//	fclose(fp2);
}