#include <iostream>

using namespace std;

int combine[26][26];
int opposed[26];
int array[100];
int oppo[26];

int turn(char c){
	int i = c-'A';
	return i;
}

char unturn(int i){
	char c = i + 'A';
	return c;
}

bool checkOppo(int curr){
	if(opposed[array[curr]] != -1 && oppo[opposed[array[curr]]] != -1){
	//	cout<<"clear "<<array[curr]<<endl;
		memset(oppo, -1, 26*sizeof(int));
		return true;
	}
	return false;
}

bool checkCombine(int curr){
//	cout<<curr<<" "<<array[curr]<<" "<<array[curr-1]<<endl;
	if(combine[array[curr]][array[curr-1]] != -1){
		oppo[array[curr]]--;
		oppo[array[curr-1]]--;
		array[curr-1] = combine[array[curr]][array[curr-1]];
		oppo[array[curr-1]]++;
//		cout<<"combine "<<array[curr-1]<<" "<<unturn(array[curr-1])<<endl;
		return true;
	}
	return false;
}

int main (int argc, char const *argv[])
{
	int T;
	int C, D, N;
	char c1, c2, c3;
	cin>>T;
	char c;
	int curr = 0;
	for(int i=0; i<T; i++){
		curr = 0;
		memset(combine, -1, 26*26*sizeof(int));
		memset(opposed, -1, 26*sizeof(int));
		memset(array, -1, 100*sizeof(int));
		memset(oppo, -1, 26*sizeof(int));
		cin>>C;
		for(int j=0; j<C; j++){
			cin>>c1>>c2>>c3;
			combine[turn(c1)][turn(c2)] = turn(c3);
			combine[turn(c2)][turn(c1)] = turn(c3);
//			cout<<"combining "<< turn(c1)<<" "<<turn(c2)<<endl;
		}
		cin>>D;
		for(int j=0; j<D; j++){
			cin>>c1>>c2;
			opposed[turn(c1)] = turn(c2);
			opposed[turn(c2)] = turn(c1);
//			cout<<"opp "<< turn(c1)<<" "<<turn(c2)<<endl;
		}
		cin>>N;
		
		for(int j = 0; j < N; j++){
			cin >> c;
//			cout <<curr<<" "<< c <<" "<< turn(c)<<endl;
			array[curr] = turn(c);
			oppo[array[curr]]++;
			curr++;
			if(curr == 1){//if the first number
				continue;
			}
			while(checkCombine(curr-1)){
				curr--;
			}
			if(checkOppo(curr-1)){
				curr = 0;
			}
		}
		
		cout<<"Case #"<<i+1<<": [";
		for(int j=0; j<curr-1; j++){
			cout<<unturn(array[j])<<", ";
		}
		if(curr != 0){
			cout<<unturn(array[curr-1]);
		}
		cout<<"]"<<endl;
	}
	
	return 0;
}