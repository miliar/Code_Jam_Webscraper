#include <stdio.h>
#include <string>
#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <vector>
#include <iostream>
#include <string>


using namespace std;

#define _CRT_SECURE_NO_WARNINGS


class RedIsGood{

public:
	
	static double getProfit(int R, int B){

		return 0;
	};
};

int main(){
	int CS=0;
	cin>>CS;
	for(int cs=0;cs<CS;cs++){
		char ipt[10][10];
		for(int i=0;i<4;i++)
			cin>>ipt[i];
		char res[1000];

		for(int i=0;i<4;i++){
			char pv=ipt[i][0];
			if(pv=='.')continue;
			int ok=true;
			for(int j=1;j<4;j++)
				if(ipt[i][j]!=pv && ipt[i][j]!='T'){
					ok=false;
					break;
				}
			if(ok){
				sprintf(res,"%c won",pv);
				goto fin;
			}
			pv=ipt[0][i];
			if(pv=='.')continue;
			ok=true;
			for(int j=1;j<4;j++)
				if(ipt[j][i]!=pv && ipt[j][i]!='T'){
					ok=false;
					break;
				}
			if(ok){
				sprintf(res,"%c won",pv);
				goto fin;
			}
		}
		char pv=ipt[0][0];
		if(pv=='.')goto NC_CK;
		bool ok=true;
		for(int i=1;i<4;i++)
			if(ipt[i][i]!=pv && ipt[i][i]!='T'){
				ok=false;
				break;
			}
		if(ok){
				sprintf(res,"%c won",pv);
				goto fin;
			}
		pv=ipt[0][3];
		if(pv=='.')goto NC_CK;
		ok=true;
		for(int i=1;i<4;i++)
			if(ipt[i][3-i]!=pv && ipt[i][3-i]!='T'){
				ok=false;
				break;
			}
		if(ok){
				sprintf(res,"%c won",pv);
				goto fin;
			}
NC_CK:

		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(ipt[i][j]=='.')
				{
				sprintf(res,"Game has not completed");
				goto fin;
			}
		sprintf(res,"Draw");
fin:
		cout<<"Case #"<<cs+1<<": "<<res<<endl;
	}

	return 0;
};

