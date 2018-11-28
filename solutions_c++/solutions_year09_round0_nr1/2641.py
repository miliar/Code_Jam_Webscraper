#include <iostream>
#include <vector>

using namespace std;
typedef vector< vector<char> > Matrix;

int main(void){
	int l,d,n;
	char c;
	cin>>l>>d>>n;
	Matrix matrix;
	for(int index=0; index<d; index++){
		vector<char> tmp;
		for(int jndex=0; jndex<l; jndex++){
			cin>>c;
			tmp.push_back(c);
		}
		matrix.push_back(tmp);
	}
	for(int index=0; index<n;index++){
		Matrix tmp2;
		int cnt=0,right=0;
		while(cnt++ < l){
			vector<char> tmp;
			bool bracket=false;
			while(true){
				cin>>c;
				if(!bracket){
					if(c=='(')	bracket=true;
					else{	tmp.push_back(c);	break;	}
				}
				else{
					if(c==')'){	bracket=false;	break;	}
					else	tmp.push_back(c);
				}
			}
			tmp2.push_back(tmp);
		}
		cnt=0;
		for(int jndex=0;jndex<d;jndex++){
			right=0;
			for(int kndex=0;kndex<l;kndex++){
				for(int hndex=0;hndex<tmp2.at(kndex).size();hndex++)
					if(tmp2.at(kndex).at(hndex)==matrix[jndex][kndex]){	right++;	break;	}
			}
			if(right==l)	cnt++;
		}
		cout<<"Case #"<< index+1<<": "<<cnt<<endl;
	}
	
	return 0;
}
