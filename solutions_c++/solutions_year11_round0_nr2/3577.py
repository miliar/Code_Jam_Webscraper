#include <iostream>
#include <string>
#include <math.h>

using namespace std;

typedef char t_pair [2];
t_pair arD [29];
int arD_count = 0;

struct s_comb {
	t_pair pair;
	char result;
};
s_comb arC [36];
int arC_count= 0;

char current[100];
int current_count = 0;

void comba(char c){
	for (int i = 0; i<arC_count; i++) {
		if ( ((c==arC[i].pair[0]) && (current[current_count-1]==arC[i].pair[1]))
			|| ((c==arC[i].pair[1]) && (current[current_count-1]==arC[i].pair[0]))) {
				current[current_count-1] = arC[i].result;
				//cout << "COMBA!!!";
				return;
		}
	}
	current[current_count++] = c;
//	cout << endl << current;
}

void destroy(){
	for (int i = 0; i<arD_count; i++) {
		int f = 0;
		int e = 0;
		for (int j=0; j<current_count; j++) {
			if (arD[i][0]==current[j]) f=1;
			else if (arD[i][1]==current[j]) e=1;
			if (f==1 && e==1) {
				current_count = 0;
				memset(current,0,sizeof(char)*100);
				return;
			}
		}
	}
};

void add(char c){
	comba(c);
	destroy();
	// дестрой
	
};
void print_current(){
	for (int j=0; j<current_count; j++) {
		cout << current[j];
		if (j!=current_count-1) cout << ", ";
	}
}

int main (int argc, char * const argv[]) {
    int t = 0, k = 1;

    cin >> t;
	while (t--) { // общее количество
		// прочитать комбы
		int i;
		arC_count = 0;
		cin >> i;
		while (i--) {
			cin.get(); // пусто перед строкой
			
			arC[arC_count].pair[0] = cin.get();
			arC[arC_count].pair[1] = cin.get();
			arC[arC_count].result = cin.get();
			
			//cout << endl << "comba:"<<arC[arC_count].pair[0] << arC[arC_count].pair[1] << arC[arC_count].result << endl;
			arC_count++;
			
		};
		// прочитать анигил
		arD_count = 0;
		cin >> i;
		while (i--) {
			cin.get();
			arD[arD_count][0] = cin.get();
			arD[arD_count][1] = cin.get();
			arD_count++;
		}
		// прочитать посимвольно строку
		current_count=0;
		memset(current,0,sizeof(char)*100);
		cin >> i;
		cin.get();
		while (i--) {			
			add(cin.get());
		}
		cout <<"Case #"<<k++ << ": [";
		print_current();
		cout <<"]"<< endl;
	}
    return 0;
}
