#include <iostream>
using namespace std;

int main(int argc, char* argv[])
{
	int L,D,N,m,sum;
	char words[5000][17], aword[15*28+2];
	bool valid0[5000], valid1[5000], hold;

	cin>>L>>D>>N;
	for (int d=0; d<D; d++) cin>>words[d];
	for (int n=1; n<=N; n++) {
		hold=false;
		for (int d=0; d<D; d++) valid0[d]=valid1[d]=false;
		cin>>aword;
		m=0;
		for (unsigned int l=0; l<strlen(aword); l++) {
			if (aword[l]=='(') hold=true;
			else if (aword[l]==')') {
				if (m>0) {
					for (int d=0; d<D; d++) {
						valid0[d]=valid1[d];
						valid1[d]=false;
					}
				}
				hold=false;
				m++;
			} else {
				if (m==0) {
					for (int d=0; d<D; d++) {
						if (words[d][0]==aword[l]) valid0[d]=true;
					}
					if (!hold) m++;
				} else {
					for (int d=0; d<D; d++) {
						if (valid0[d] && words[d][m]==aword[l])
							valid1[d]=true;
					}
					if (!hold) {
						for (int d=0; d<D; d++) {
							valid0[d]=valid1[d];
							valid1[d]=false;
						}
						m++;
					}
				}
			}
		}
		sum=0;
		for (int d=0; d<D; d++) if (valid0[d]) sum++;
		cout<<"Case #"<<n<<": "<<sum<<endl;
	}
	return 0;
}

