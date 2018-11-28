#include <iostream>
#include <set>
#include <string>
#include <cstring>
using namespace std;

set<string> sd;

int main(){
//	FILE *fin = stdin;
//	FILE *fout = stdout;
 	FILE *fin = fopen("A-large.in","r");
 	FILE *fout = fopen("RoundBLarge.out","w");
	
	int t,tt,m,n,i,j;
	fscanf(fin,"%d",&t);
	tt = 0;
	while(t--){
		tt++;
		sd.clear();
		fscanf(fin,"%d %d",&n,&m);
		for(i = 0; i < n; i++)
		{
			char temp[200];
			fscanf(fin,"%s",temp);
			string tmp(temp,temp+strlen(temp));
			sd.insert(tmp);
		}

		int ans = 0;
		for(i = 0; i < m; i++)
		{
			char temp[200];
			fscanf(fin,"%s",temp);

			int index = 1,s = strlen(temp);
			while(index < s){
				while(temp[index] != '/' && index < s){
					index++;
				}
				string tmp(temp,temp+index);
				if(sd.find(tmp) == sd.end()){
					sd.insert(tmp);
					ans++;
				}
				index++;
			}
		}
		fprintf(fout,"Case #%d: %d\n",tt,ans);

	}


	return 0;
}