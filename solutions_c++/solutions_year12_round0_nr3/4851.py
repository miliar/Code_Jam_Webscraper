#include<iostream>
#include<cmath>
using namespace std;
int n,a,b,i,e,f;
int d[10];
int reset(){
for (int x=0;x<10;x++)d[x]=0;
}

int dig(int x){
	int c=0;
	while(x>0){
		x=x/10;
		c++;
	}
	return c;
}

int main(){
	cin>>n;
	i=n;
	while(i>0){
		cin>>a>>b;
		int count1=0;
	
	for(int x=a;x<=b;x++){
				int c=dig(x);
				int count=0;
				reset();
				d[0] =f=x;
				int s=1;
			while(count<c-1){
			
				e = (f%10)*pow(10,c-1)+f/10; 
				if(f%10!=0){
				int flag=0;
				int k=0;
				while(d[k]!=0){
					if(d[k]==e){
					flag =1;
				break;
					}
					k++;
				}
				if(flag==0&&a<=e&&e<=b){
				
				d[s]=e;
				s++;
				}
				else if (flag==1); //break;
				}
				count++;
				f=e;
			}
	count1+=s-1;
}	
i--;
cout<<"case #"<<(n-i)<<": "<<(count1/2)<<endl;
} 
}
