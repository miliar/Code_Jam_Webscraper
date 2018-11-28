#include<iostream>
#include<cstdlib>
#include<string>
#include<queue>
using namespace std;

struct Data{
	int ba;
	char d;
};

main(){
	
	int n;
	
	scanf("%d",&n);
	
	for(int i = 0;i < n;++i){
		
		int o1 = 1,b1 = 1;
		
		int tn,ans = 0;
		queue<Data> zenbu,O,B;
		
		scanf("%d",&tn);
		
		for(int i = 0;i < tn;++i){
			
			int tmp;
			char tmp2[10];
			
			scanf("%s %d",tmp2,&tmp);
			
			Data t = {tmp,tmp2[0]};
			
			zenbu.push(t);
			if(tmp2[0] == 'O')O.push(t);
			else B.push(t);
		}
		
		Data o ,b;
		
		for(int i = 0;i < tn;++i){
			Data Q = zenbu.front();
			zenbu.pop();
			if(O.size() != 0) o = O.front();
			if(B.size() != 0) b = B.front();
			//printf("Qba = %d bba = %d oba = %d\n",Q.ba,b.ba,o.ba);
			
			if(Q.d == 'O'){
				int kyori = abs(o1 - Q.ba);
				//printf("kyori = %d ",kyori);
				ans += kyori + 1;
				
				o1 = Q.ba;
				O.pop();
				
				if(kyori +1 >= abs(b.ba - b1))b1 = b.ba;
				else{
					if(abs(b.ba - (b1 + kyori + 1)) >  abs(b.ba - (b1 - (kyori + 1)))){
						b1 -= kyori + 1;
					}
					else{
						b1 += kyori + 1;
					}
				}
			
			}
			else{
				int kyori = abs(b1 - Q.ba);
				//printf("kyori = %d ",kyori);
				ans +=  kyori + 1;
				
				b1 = Q.ba;
				B.pop();
				
				if(kyori +1 >= abs(o.ba - o1))o1 = o.ba;
				else{
					if(abs(o.ba - (o1 + kyori + 1)) >  abs(o.ba - (o1 - (kyori + 1)))){
						o1 -= kyori + 1;
					}
					else{
						o1 += kyori + 1;
					}
				}
			}
			
			//printf("O.ba = %d B.ba = %d ans = %d\n",o1,b1,ans);
			
		}
		
		printf("Case #%d: %d\n",i+1,ans);
	}
}