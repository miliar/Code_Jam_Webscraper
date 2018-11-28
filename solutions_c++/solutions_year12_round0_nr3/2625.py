#include <iostream>
#include <math.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int i=1;
	while(i<=t){
		int a;
		int b;
		int count = 0;
		cin>>a;
		cin>>b;
		int arr[2000001]={0};
		for(int m = a;m<=b;m++){
			arr[m]=1;
		}
		int d=0;
		int x=b;
		while(x>0){
			x = x/10;
			d++;
		}
	//	cout<<d;
		int dig = d;
		d = pow(10,d-1);
//		cout<<d;
		int v[dig];
		for(int h=0;h<dig;h++){
			                                v[h]=0;
							                        }

		int j;
		for(j=a;j<b;j++){
//			cout<<"loop"<<endl;
			int no = j;
			int u=0;
			
			for(int y = 0;y<dig;y++){
				                                arr[v[y]]=1;
								                        }

		//	for(int h=0;h<dig;h++){
		//		v[h]=0;
		//	}
			arr[j]=1;
	//		for(int y = 0;y<dig;y++){
	//			arr[v[y]]=1;
	//		}
			if(arr[j]==2){
			//	cout<<"cont";
				continue;
			}
//			cout<<"here"<<endl;
			arr[j]=2;
			for(int k=1;k<dig;k++){
				int l = no%10;
				no = l*d + no/10;
				
		//		cout<<no<<endl;
				if(no<=b){
				if(arr[no]==1){
//					cout<<no<<endl;
					count++;
					arr[no]=2;
					v[k-1]=no;
				}
				}
			}
		}
		cout<<"Case #"<<i<<": "<<count<<endl;
		i++;
	}
	return 0;
}




