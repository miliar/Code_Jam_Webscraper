#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <string>
#include <map>
#include <math.h>
#include <stack>
#include <bitset>

using namespace std;


#define ii pair<int,int>
#define iii pair<int,ii>
typedef long long ll;
typedef unsigned long long ull;

char peta[6][6];
bool x,o;

void cekV(){

	if(x==true || o==true){return ;}


	for(int i=0;i<4;i++)
	{
		int jumlah_x=0,jumlah_o=0,jumlah_t=0;

		for(int j=0;j<4;j++){

			if(peta[i][j]=='X'){jumlah_x++;}
			else if(peta[i][j]=='O'){jumlah_o++;}
			else if(peta[i][j]=='T'){jumlah_t++;}

		}

		if(jumlah_x==4){x=true;return;}
		if(jumlah_o==4){o=true;return;}

		if(jumlah_x==3 && jumlah_t==1){x=true;return;}
		if(jumlah_o==3 && jumlah_t==1){o=true;return;}

	}

}

void cekH(){

	if(x==true || o==true){return ;}


	for(int i=0;i<4;i++)
	{
		int jumlah_x=0,jumlah_o=0,jumlah_t=0;

		for(int j=0;j<4;j++){

			if(peta[j][i]=='X'){jumlah_x++;}
			else if(peta[j][i]=='O'){jumlah_o++;}
			else if(peta[j][i]=='T'){jumlah_t++;}

		}

		if(jumlah_x==4){x=true;return;}
		if(jumlah_o==4){o=true;return;}

		if(jumlah_x==3 && jumlah_t==1){x=true;return;}
		if(jumlah_o==3 && jumlah_t==1){o=true;return;}

	}

}

void cekDB(){

	if(x==true || o==true){return ;}

	int jumlah_x=0,jumlah_o=0,jumlah_t=0;

	for(int i=0;i<4;i++)
	{


			if(peta[i][i]=='X'){jumlah_x++;}
			else if(peta[i][i]=='O'){jumlah_o++;}
			else if(peta[i][i]=='T'){jumlah_t++;}

	}


		if(jumlah_x==4){x=true;return;}
		if(jumlah_o==4){o=true;return;}

		if(jumlah_x==3 && jumlah_t==1){x=true;return;}
		if(jumlah_o==3 && jumlah_t==1){o=true;return;}

}

void cekDA(){

	if(x==true || o==true){return ;}

	int jumlah_x=0,jumlah_o=0,jumlah_t=0;

	for(int i=0,j=3;i<4;i++,j--)
	{




			if(peta[i][j]=='X'){jumlah_x++;}
			else if(peta[i][j]=='O'){jumlah_o++;}
			else if(peta[i][j]=='T'){jumlah_t++;}



	}

	if(jumlah_x==4){x=true;return;}
		if(jumlah_o==4){o=true;return;}

		if(jumlah_x==3 && jumlah_t==1){x=true;return;}
		if(jumlah_o==3 && jumlah_t==1){o=true;return;}

}

int main (){

	freopen("input.txt","r",stdin);	freopen("iseng.txt","w",stdout);

	int t;
	int jumlah_kotak;

	scanf("%d",&t);getchar();

	for(int kasus=1;kasus<=t;kasus++){

		jumlah_kotak=0;

		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%c",&peta[i][j]);
				if(peta[i][j]!='.')jumlah_kotak++;
			}
			getchar();
		}

		getchar();

		x=o=false;

		cekV();
		cekH();
		cekDA();
		cekDB();

		printf("Case #%d: ",kasus);

		if(x==true){
			printf("X won\n");
		}
		else if(o==true){
			printf("O won\n");
		}
		else if(jumlah_kotak==16){
			printf("Draw\n");
		}
		else {
			printf("Game has not completed\n");
		}


	}



}



