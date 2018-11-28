#include<iostream>
using namespace std;

int main(){
	int t,kase=1,k;
	cin>>t;
	while(t--){
		int c,d,n,i;
		cin>>c;
		char comb[1][3];
		for(i=0;i<c;i++){
			cin>>comb[i][0]>>comb[i][1]>>comb[i][2];
		}
		cin>>d;
		char dest[1][2];
		for(i=0;i<d;i++)
			cin>>dest[i][0]>>dest[i][1];
		cin>>n;
		char seq[n],out[n],cmbchar='\0',destchar='\0';
		k=0;
		//cout<<"c="<<c<<" d="<<d<<" n="<<n<<endl;
		for(i=0;i<n;i++)
			cin>>seq[i];
		for(i=0;i<n;i++)
		{
			/*cout<<i<<":[";
				for(int m=0;m<k;m++)
					cout<<out[m]<<", ";
				cout<<endl;*/
				if(destchar!='\0'){
					if(d>0){
						if(seq[i]==dest[0][1]){
							if(destchar==dest[0][0]){
								k=0;
								destchar='\0';
								continue;
							}
						}
						if(seq[i]==dest[0][0]){
							if(destchar==dest[0][1]){
								k=0;
								destchar='\0';
								continue;
							}
						}
					}
					
				}
				if(c>0){
					if(seq[i]==comb[0][0] && seq[i+1]==comb[0][1])
					{
							out[k++]=comb[0][2];
							i++;
							continue;
					}
					if(seq[i]==comb[0][1] && seq[i+1]==comb[0][0])
					{
							out[k++]=comb[0][2];
							i++;
							continue;
					}
				}
				if(d>0){
					if(seq[i]==dest[0][1]){
						destchar=seq[i];
					}
					if(seq[i]==dest[0][0]){
						destchar=seq[i];
					}
				}
				out[k++]=seq[i];
				
		}
		cout<<"Case #"<<kase++<<": [";
		for(int m=0;m<k-1;m++)
			cout<<out[m]<<", ";
		cout<<out[k-1]<<"]"<<endl;	
	}
}
