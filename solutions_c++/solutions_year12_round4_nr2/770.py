#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;



int T,n,w,l,r[1111];
int main(){
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	cin >> T;
	for(int Case = 1; Case <= T ;Case ++){
		scanf("%d %d %d",&n,&w,&l);
		int x=0;
		for(int i = 0;i < n; i++){
			scanf("%d",&r[i]);
			if(r[i]>x)x = r[i];
		}
		printf("Case #%d: ",Case);
		int y = r[0];
		printf("0 0");
		int xx = 0;
		for(int i = 1 ; i < n; i++){
			y += r[i];
			if(w > l)
			{
				if(y > w){
					y = 0;
					xx = 2*x;
				}
				printf(" %d %d",y,xx);
				
			//	if(y > w)cout<<"!!"<<endl;
			}
			else{
					if(y > l){
					y = 0;
					xx = 2*x;
				}
				printf(" %d %d",xx,y);
			//	if(y > l)cout<<"!!"<<endl;
			}
			y += r[i];
		}
		printf("\n");
	

	}

	return 0;
}
