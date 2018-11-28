
#include <iostream>
using namespace std;

char map[4][4];
char tmp;
int num[256];
char checkrow(){

	for(int i=0; i<4; ++i){
	memset(num,0,sizeof(num));
	for(int j=0; j<4; ++j){
		num[map[i][j]]++;
	}
	if(num['X']>=3&&num['O']==0) return 'X';
	if(num['O']>=3&&num['X']==0) return 'O';
	}
	return 'Y';
	
}
char checkcol(){
	for(int i=0; i<4; ++i){
	memset(num,0,sizeof(num));
	for(int j=0; j<4; ++j){
		num[map[j][i]]++;
	}
	if(num['X']>=3&&num['O']==0) return 'X';
	if(num['O']>=3&&num['X']==0) return 'O';
	}
	return 'Y';
}
char checkdig(){
	
	memset(num,0,sizeof(num));
	for(int i=0; i<4; ++i){
		num[map[i][i]]++;
	}
	if(num['X']>=3&&num['O']==0) return 'X';
	if(num['O']>=3&&num['X']==0) return 'O';
	memset(num,0,sizeof(num));
	for(int i=0; i<4; ++i){
		num[map[i][3-i]]++;
	}
	if(num['X']>=3&&num['O']==0) return 'X';
	if(num['O']>=3&&num['X']==0) return 'O';
	return 'Y';

}
int main(){
    int t,cnt=0;
    
	freopen("A-small-attempt4.in","r",stdin);
	freopen("1.out","w",stdout);
	cin>>t;
    while(t--){
		cin.ignore();
		bool finish=1;
               for(int i=0; i<4; ++i){
                       cin.get(map[i],5);
                       cin.ignore();
                       }
			   for(int i=0; i<4; ++i){
				   for(int j=0; j<4; ++j){
					   if(map[i][j]=='.') finish=0;
				   }
	}
			   char ans=checkrow();
			   if(ans=='Y') ans=checkcol();
			   if(ans=='Y') ans=checkdig();
			   cout<<"Case #"<<++cnt<<": ";
			   if(ans!='Y') cout<<ans<<" won"<<endl;
			   else if(finish) cout<<"Draw"<<endl;
			   else cout<<"Game has not completed"<<endl;
	}
               
    }
