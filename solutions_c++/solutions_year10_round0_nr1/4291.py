#import <Foundation/Foundation.h>
#import <fstream.h>
using namespace std;
struct Snapper
{
public:
	bool plugged;
	bool state;
	Snapper():state(0), plugged(0){};
	
};

int main (int argc, char const *argv[]){
	ifstream in("input.txt");
	ofstream out("output.txt");
	int T;
	in>>T;
	for(int casenr = 1; casenr <= T; casenr++){
		int N, K;
		in>>N>>K;
		Snapper s[N];
		s[0].plugged=1;
		printf("\n");
		for(int i = 0; i <= K-1; i++){
			for(int j=0; j<=N-1; j++){
				if(s[j].plugged){
					if(s[j].state)
						s[j].state=0;
					else
						s[j].state=1;
				}
			}
			int flag=1;
			for(int g=0; g<=N-1; g++){
				if(s[g].state&&flag)
					s[g+1].plugged=1;
				else{
					s[g+1].plugged=0;
					flag=0;
				}
			}
			
			//for(int g=0; g<=N-1; g++)
			//	printf("%i%i ", s[g].state, s[g].plugged);
			//printf("\n");
		}
		out<<"Case #"<<casenr<<": ";
		if(s[N-1].plugged&&s[N-1].state)
			out<<"ON\n";
		else
			out<<"OFF\n";
	}
	return 0;
}