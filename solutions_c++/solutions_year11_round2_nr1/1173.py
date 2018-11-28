#include<iostream>
#include<vector>
#include<iomanip>
using namespace std;
int main()
{
	int T;
	cin >> T;
	for(int t=1;t<=T;t++)
	{
		int s;
		cin >> s;
		cout << setprecision (12);
		string tmp;
		getline(cin,tmp);
		vector<string> v(s);
		for(int i=0;i<s;i++)
		{
			getline(cin,tmp);
			v[i]=tmp;
		}
		vector <double> WP(s);
		vector <double> OWP(s);
		int win;
		int grane;
		for(int i=0;i<s;i++)
		{
			win=0;
			grane=0;
			for(int j=0;j<s;j++)
			{
				if(v[i][j]=='1')
				{
					win++;
					grane++;
				}
				if(v[i][j]=='0')
					grane++;
			}
			WP[i]=double(win)/grane;
			//cout << WP[i] << endl;
		}
		double AWP=0;
		for(int i=0;i<s;i++)
		{
			AWP+=WP[i]/s;
		}
//		cout << AWP << endl;
		vector <int> meczy(s);
		for(int i=0;i<s;i++)
			for(int j=0;j<s;j++)
				if(v[i][j]=='0' || v[i][j]=='1')
					meczy[i]++;
		for(int i=0;i<s;i++)
		{
			int c=0;
			OWP[i]=0;
			for(int j=0;j<s;j++)
			{
				if(v[i][j]!='.')
					c++;	
			}
			for(int j=0;j<s;j++)
			{
				if(v[i][j]=='1')
					OWP[i]+=WP[j]*meczy[j]/(meczy[j]-1);
				if(v[i][j]=='0')
					OWP[i]+=(WP[j]*meczy[j]-1)/(meczy[j]-1);
			}
			OWP[i]=OWP[i]/meczy[i];
//			cout << "O" << OWP[i] << endl;
		}
		vector <double> OOWP(s);
		for(int i=0;i<s;i++)
		{
			OOWP[i]=0;
			for(int j=0;j<s;j++)
				if(v[i][j]=='1'||v[i][j]=='0')
				{
					OOWP[i]+=OWP[j];
				}
			OOWP[i]=OOWP[i]/meczy[i];
//			cout << "OO " << OOWP[i] << endl;
		}
		cout << "Case #" << t<< ": \n";
			for(int i=0;i<s;i++)
				cout<< 0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i] << "\n";

	}
}
