#include<stdio.h>
#include<malloc.h>
#include<list>
#include<string>
using namespace std;
int main(){
	int T,C,D,N;
	char combine[50][100];
	char opposed[50][100];
	char input[200];
	char a,b,c;
	int flag,newflag,i,j,k;
	list<char> output;
	scanf("%d",&T);
	list<char>::iterator p;	
int yash;
	for(yash=1;yash<=T;yash++){
		output.clear();
		scanf("%d",&C);
		for(i=0;i<C;i++){
			scanf(" %s",combine[i]);
		}
		scanf("%d",&D);
		for(i=0;i<D;i++){
			scanf( "%s",opposed[i]);
		}
		scanf("%d",&N);
		scanf(" %s",input);
		for(i=0;i<N;i++){
			if(output.empty()){
				output.push_back(input[i]);
				continue;
			}
			else{
				a=output.back();
				flag=0;
				for(j=0;j<C;j++){
					if((combine[j][0]==a&&combine[j][1]==input[i])||(combine[j][0]==input[i]&&combine[j][1]==a)){
						output.pop_back();
						output.push_back(combine[j][2]);
						flag=1;
						break;
					}
				}
				if(flag==0){
					newflag=0;
					p=output.begin();
					while(p!=output.end()){
						for(j=0;j<D;j++){
							if((opposed[j][0]==input[i]&&opposed[j][1]==*p)||(opposed[j][0]==*p&&opposed[j][1]==input[i])){
								newflag=1;
								output.clear();
								break;
							}
						}
						if(newflag==1)
							break;
						p++;
					}
				}
				if(flag==0&&newflag==0)
					output.push_back(input[i]);
			}


		}

	if(output.size()>=1){
	printf("Case #%d: [",yash);
        
	p=output.begin();
	for(k=0;k<output.size()-1;k++){
	printf("%c, ",*p);
	p++;
	}
	printf("%c]\n",*p);
	}
	else printf("Case #%d: []\n",yash);
	}
return 0;
}
