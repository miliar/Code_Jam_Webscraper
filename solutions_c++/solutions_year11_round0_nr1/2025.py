#include<iostream>
#include<vector>
#include<string>
using namespace std;

int ntests;

int n;
vector<int> b,o,r;
string rseq;


int main()
{
	cin>>ntests;
	for(int ii=0;ii<ntests;ii++)
	{
		cin>>n;
		b.clear();
		o.clear();
		r.clear();
		rseq = "";
		
		for(int i=0;i<n;i++){
			char ch ;
			int button;
			cin>>ch>>button;
			if(ch == 'B')b.push_back(button);
			if(ch == 'O')o.push_back(button);
			rseq =  rseq + ch;
			r.push_back(button);
		}

			int t=0,b1=0,o1=0,r1=0,bp=1,op=1;
			for(t=1;o1<o.size()||b1<b.size();t++)
			{
				if(rseq[r1]=='O'){
					if(o[o1]==op){
						o1++;
						r1++;
					} else {
						if(o[o1]>op)op++;
						else if(o[o1]<op)op--;
					}
					if(b1<b.size()){
						if(b[b1]>bp)bp++;
						else if(b[b1]<bp)bp--;
					}
				}else{
					if(b[b1]==bp){
						b1++;
						r1++;
					}
					else {
						if(b[b1]>bp)bp++;
						else if(b[b1]<bp)bp--;
					}
					if(o1<o.size()){
						if(o[o1]>op)op++;
						else if(o[o1]<op)op--;
					}
				}
			}

			cout<<"Case #"<<ii+1<<": "<<t-1<<endl;
		
	}
}