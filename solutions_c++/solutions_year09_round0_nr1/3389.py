#include<iostream>
#include<string>

using namespace std;
int main(){

freopen("aki.in","r",stdin);
freopen("a.out","w",stdout);
int l,d,n;
cin>>l>>d>>n;
char niz[100][5000];
int i,j;
for(i=0;i<d;i++)
for(j=0;j<l;j++)cin>>niz[i][j];

int x,k,brojac,pok,pok1,y=0;
string rec;
for(k=0;k<n;k++){
cin>>rec;
//cout<<kurc[0]<<niz[0][0]<<endl;
brojac=0;pok=0;

for(i=0;i<d;i++){pok=0;x=1;y=0;//pazi stavi ispod da je x=1
	for(j=0;j<l;j++){
		if(rec[pok]==niz[i][j]){pok++;continue;}
		else  if(rec[pok]=='('){

			  while(rec[++pok]!=')')
				  if(rec[pok]==niz[i][j]){x=1;while(rec[++pok]!=')');pok++;break;}
				  else x=0;

		} else x=0;
	 }
if(x>=1)brojac++;pok++;
}





cout<<"Case #"<<k+1<<": "<<brojac<<endl;

}

return 0;

}

