#include <iostream>

using namespace std;

int main()
{
	int T, A, B, flag, output;
	cin>>T;
	for(int i=0;i<T;i++) {
		cin>>A>>B;
		output=0;
		flag=0;
		if(A/10>0&&A/100==0) {
			for(int p=A/10;p<=B/10;p++) {
				for(int q=p+1;q<=9;q++) {
					if(p*10+q>B) {
						flag=1;
						break;
					}
					else if(p*10+q<A)
						q=A%10;
					if(q*10+p<=B){
						output++;
					}
					else
						break;
				}
				if(flag)
					break;
			}
		}
		else if (A/1000==0) {
			for(int p=A/100;p<=B/100;p++) {
				for(int q=0;q<=9;q++) {
					for(int r=p>q?p:p+1;r<=9;r++) {
						if(p*100+q*10+r>B) {
							flag=1;
							break;
						}
						else if(p*100+q*10+r<A) {
							q=(A/10)%10;
							if(p<=q)
								r=p+1;
							if(r<A%10)
								r=A%10;
						}
						if(r*100+p*10+q<=B) {
							output++;
						}
						else
							break;
					}
					if(flag)
						break;
				}
				if(flag)
					break;
			}
			flag=0;
			for(int p=A/100;p<=B/100;p++) {
				for(int q=p;q<=9;q++) {
					for(int r=(p<q)?0:p+1;r<=9;r++) {
						if(p*100+q*10+r>B) {
							flag=1;
							break;
						}
						else if(p*100+q*10+r<A) {
							q=(A/10)%10;
							r=A%10;
						}
						if(q*100+r*10+p<=B) {
							output++;
						}
						else
							break;
					}
					if(flag)
						break;
				}
				if(flag)
					break;
			}
		}
		cout<<"Case #"<<i+1<<": "<<output<<"\n";
	}
	return 0;
}
