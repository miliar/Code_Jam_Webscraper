#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class largeNumber{
public: char num[60];
};

bool less_largeNumber(const largeNumber & a, const largeNumber & b) { //a<bÊ±·µ»Øtrue
    bool less = true;
	if (strlen(a.num)>strlen(b.num)) {
		less = false;
	}else if(strlen(a.num)==strlen(b.num)){
		if (strcmp(a.num,b.num)>=0) { //if a larger than b, return 1,else not
			less = false;
		}
	}
	return less;
}


largeNumber operator -(largeNumber& a,largeNumber& b)
{ 
	largeNumber result;

	int direction = 1,i;
	if (strlen(a.num)>strlen(b.num)) {
		direction = 0;
	}else if(strlen(a.num)==strlen(b.num)){
		if (strcmp(a.num,b.num)==1) { //if a larger than b, return 1,else not
			direction = 0;
		}else if (strcmp(a.num,b.num)==0)
			direction = 2;
	}

	char * big,*small;
	if (direction == 0){
		big = a.num;
		small = b.num;
	}else if (direction == 1){
		big = b.num;
		small = a.num;
	}else{
		strcpy(result.num,"0");
		return result;
	}
	int smalllen = strlen(small);
	int biglen = strlen(big);
	strcpy(result.num,big);
	for(i=1;i<=smalllen;i++){
		result.num[biglen-i] = result.num[biglen-i] + 48 - small[smalllen-i];			
	}
	for(i=1;i<=biglen;i++){
		if (result.num[biglen-i] < 48) {
			result.num[biglen-i] += 10;
			result.num[biglen-i-1] -= 1;
		}
	}	
	for(i=0;i<biglen;i++){
		if (result.num[i] > 48)
			break;
		else if (result.num[i] < 48){
			cout<<"error\n";
			break;
		}		
	}
	char * p = result.num + i;
	if (i > 0){
		char temp[60];
		strcpy(temp, p);
		strcpy(result.num , temp);
	}
    return result; 
}  


largeNumber f(largeNumber& a,largeNumber&b){	
	while((strcmp(a.num,"0") != 0) && (strcmp(b.num,"0") != 0)){
		if (less_largeNumber(a,b)){
			b = b-a;
		}
		else {
			a =a-b;
		}
	}
	return (a-b);
}


int main(int argc, char *argv[]){
	int i,j;
	largeNumber input;

	vector<largeNumber>  vect;

	ifstream in("B-small-attempt2.in");
	ofstream out("B-small-attempt2.out");
	int C,N;
	in>>C;
	for (i=0;i<C;i++){
		vect.clear();
		in>>N;
		for(j=0;j<N;j++){
			in>>input.num;
			vect.push_back(input);
			//cout<<vect[j].num<<' ';
		}
		//cout<<endl;
		
		sort(vect.begin(), vect.end(), less_largeNumber);
		largeNumber smallest = vect[0];
		N--;
		for(j=0;j<N;j++){		
			vect[j] = vect[j+1] - vect[j];
			//cout<<vect[j].num<<' ';
		}

		while (N > 1) {
			for (j=0;j<N-1;j++){
				vect[j] = f(vect[j],vect[j+1]);
			}
			N--;
		}
		while(less_largeNumber(vect[0],smallest))
			smallest = smallest- vect[0];
		smallest = vect[0] - smallest;


		out<<"Case #"<<i+1<<": "<<smallest.num<<endl;
	}

}