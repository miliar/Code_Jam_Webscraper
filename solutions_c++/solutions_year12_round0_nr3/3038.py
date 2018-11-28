#include<iostream>
#include<fstream>
using namespace std;
void main(){
	ofstream cout("test.txt");
	int T;
	cin >> T;
	int A,B;
	int digit[20];
	for(int i = 0; i < T; i++){
		int count = 0;
		cin >> A >> B;
		if(B>=10){
			int tB = B;int tBc = 0;int frB = 0;
			while(tB){frB = tB%10;tB/=10;tBc++;}
			frB/=2;frB+=1;
			while(tBc--)frB*=10;
			for(int j = A; j <= frB; j++){
				int tj = j;int k = 0;
				while(tj){
					digit[k++]=tj%10;
					tj/=10;
				}
				for(int tk = 0; tk < k-1; tk++){
					digit[tk+k]=digit[tk];
					if(digit[tk+k]==0)continue;
					else{
						int tr = 0;
						int tkk = tk+k;
						while(tkk>=tk+1){
							tr*=10;
							tr+=digit[tkk--];
						}
						if(tr<=B&&tr>j){
							count++;
						}
					}
				}
			}
		}
		else{}
		cout << "Case #"<<i+1<<": "<<count<<endl;
	}
	system("pause");
}