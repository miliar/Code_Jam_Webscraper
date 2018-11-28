//google jam 3
#include <iostream>
#include <fstream>
using namespace std;

int main(){
	int pre[31][2];
	
	//the highest score could reach with surprise
	pre[0][0]=pre[1][0]=pre[29][0]=pre[30][0]=-1;
	for (unsigned int i=3;i<30;i=i+3){
		pre[i-1][0]=(i/3)+1;
		pre[i][0]=(i/3)+1;
		pre[i+1][0]=(i/3)+1;
	}
	
	//the highest score could reach without surprise
	pre[0][1]=0;
	for (unsigned int i=3;i<33;i=i+3){
		pre[i-2][1]=i/3;
		pre[i-1][1]=i/3;
		pre[i][1]=i/3;
	}
	
	int T,N,S,p;
	
	ifstream input("B-large.in");
	ofstream output("out.txt");
	
	input >> T; // number of cases
	for (unsigned int i=0;i<T;i++){
		bool flag=false;
		input >> N; // number of googlers
		input >> S; // surprising
		input >> p; //the highest score
		int googler[N];
		int a=0; // who always reach standard
		int b=0; // who could reach stander by having a surprise
		int c=0; // who will never reach standard
		for (unsigned int j=0;j<N;j++){
			input >> googler[j];
			if (pre[googler[j]][1]>=p) a++;
			if (pre[googler[j]][1]<p && pre[googler[j]][0]>=p) b++;
			if (pre[googler[j]][1]<p && pre[googler[j]][0]<p) c++;
		}
		int ans;
		if (S>=b) ans = a + b;
		else ans = a + S;
		output << "Case #"<<i+1<<": " << ans << endl;
	}
	return 0;
}
