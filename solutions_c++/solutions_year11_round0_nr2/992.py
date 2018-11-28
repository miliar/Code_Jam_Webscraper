#include "cstdio"
#include "iostream"
#include "vector"
#define mp make_pair
using namespace std;

class Magicka{

	private:
		vector<pair<char,char> > com, opp;
		vector<char> form, missing;
		vector<char> list;
		FILE *input; 
		FILE *output;
	public: 
		Magicka(){
			input = fopen ("B-large.in","r");
			output = fopen ("outlarge","w");	
		}
		void read();
		void check_elements();	
		void show_list(int t);
};

void Magicka::show_list(int t){
	int n;
	fprintf(output,"Case #%d: [",t);
	n = list.size()-1;
	for(int i=0;i<n;i++)
		fprintf(output,"%c, ",list[i]);
	if(n!=-1) fprintf(output,"%c",list[n]);
	fprintf(output,"]\n");
}

void Magicka::check_elements(){
	
	int m = list.size();
	char a,b;

	// if more than 1 element look for combines and opposed
	if(m < 2)return;
	a = list[m-2];
	b = list[m-1];

	// loking for combines
	m = com.size();
	for(int i=0;i<m;i++){
		if( (com[i].first == a && com[i].second == b) || (com[i].second == a && com[i].first == b)){
			list.pop_back();
			list.pop_back();
			list.push_back(form[i]);
			return;
		}
	}

	// loking for opposed
	m = opp.size();
	for(int i=0;i<m;i++){
		if( (opp[i].first == b && opp[i].second == a) || (opp[i].first == a && opp[i].second == b)){
			list.clear();
			missing.clear();
			return;
		}
	}

	m = missing.size();
	for(int i=0;i<m;i++){
		if(missing[i] == b || missing[i] == a){
			list.clear();
			missing.clear();
			return;
		}
	}

	m = list.size();
	b = list[m-2];
	// updating missing list
	m = opp.size();
	for(int i=0;i<m;i++){
		if(opp[i].first == b){
			missing.push_back(opp[i].second);
		}
		else if(opp[i].second == b){
			missing.push_back(opp[i].first);
		}
	}
}

void Magicka::read(){
	
	int t,n;
	char c1,c2,c3,last;

	// for each test
	fscanf(input,"%d",&t);

	for (int j=1; j<=t; j++){	

		last = NULL;
		// combines
		fscanf(input,"%d ",&n);
		for (int i=0; i<n; i++){
			fscanf(input,"%c%c%c ",&c1,&c2,&c3);
			com.push_back(mp(c1,c2));
			form.push_back(c3);
		}

		// opposed
		fscanf(input,"%d ",&n);
		for (int i=0; i<n; i++){
			fscanf(input,"%c%c ",&c1,&c2);
			opp.push_back(mp(c1,c2));
		}

		// elements to invoke
		fscanf(input,"%d ",&n);
		for (int i=0; i<n; i++){
			fscanf(input,"%c",&c1);
			list.push_back(c1);
			check_elements();
		}
		show_list(j);
		com.clear();
		opp.clear();
		form.clear();
		list.clear();
		missing.clear();
	}
}

int main(){

	Magicka magician;
	magician.read();

	return 0;
}