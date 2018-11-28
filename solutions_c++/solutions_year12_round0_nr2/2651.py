#include <iostream>
#include <string>
#include <cstdlib>
#include<cstdio>

using namespace std;

int main(){
    int a,surp,b,count,num,out=0;
    scanf("%d",&count);
    for(int i=0;i<count;i++){
	out=0;
    	scanf("%d %d %d",&a,&surp,&b);
	for(int j=0;j<a;j++){
	   scanf("%d",&num);
	   if(num/3>=b){out++;
	   }else if(num%3==1&& num/3+1>=b){out++;
	   }else if(num%3==2&& num/3+1>=b){out++;
	   }else if(num%3==0&& num/3+1>=b && surp!=0 && num/3>1){out++;surp--;
     	   }else if(num%3==1&& num/3+2>=b && surp!=0 && num/3>1){out++;surp--;
	   }else if(num%3==2&& num/3+2>=b && surp!=0){out++;surp--;
	   }else{} 
	}
	cout<<"Case #"<<i+1<<": "<<out<<endl;
    }

}
