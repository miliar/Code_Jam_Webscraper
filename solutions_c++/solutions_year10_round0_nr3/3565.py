#include <iostream>
#include <vector>

using namespace std;

int main()
{
	vector<long long> v;
	int testcase;
	cin>>testcase;
	for(int iii=0;iii<testcase;iii++){
	//	cout<<"New test case"<<endl;
		long long r,k,n;
		vector <long long > v;
		cin>>r>>k>>n;
	//	cout<<"Rides = "<<r<<" Max ppl = "<<k<<" No of Groups "<<n<<endl;
		long long start=0,current=0;
		long long temp=0;
		long long count=0;
	//	cout<<"Input: ";
		for(int i=0;i<n;i++){
			long long t1;
			cin>>t1;
	//		cout<<t1<<" ";
			v.push_back(t1);
		}
	//	cout<<endl;
		long long total=0;
		for(int i=0;i<r;i++){
	//		cout<<"Starting with "<<start<<endl;
			current=start;			
			while( temp < k && count < n ){
				if( (temp+v[current])<=k){
	//				cout<<"Adding group "<<current<<" with people "<<v[current]<<endl;
					total+=v[current];
					temp+=v[current++];
					count++;
					if(current==n){
						current =0;
					}
				} else {
					break;
				}
			}
	//		cout<<" End of Ride "<<i+1<<" : people = "<<temp<<" groups = "<< count << " next start group "<<current<<endl;
			temp=0;
			count=0;
			start=current;
		}
		cout<<"Case #"<<iii+1<<": "<<total<<endl;
	}
}

			
			
					
	
