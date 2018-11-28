#include <iostream>


using namespace std;

void read_input();
bool solution(int index);
int antal =0;
int **input_array;

FILE *ouput_file =fopen("answer.out","w");

int main(){
	
	read_input();
	for (int i=0;i<antal;i++){
	
		if (solution(i)==true){
		//printf("Case #%i: ON \r\n",i);
		fprintf(ouput_file,"Case #%i: ON \r\n",(i+1));
		}else{

		//printf("Case #%i: OFF\r\n",i);
		fprintf(ouput_file,"Case #%i: OFF \r\n",(i+1));
		}

		
	
	}

	return 0;
}

bool solution(int index){
	
	int lamper= input_array[index][0];
	int temp = input_array[index][1];

	for (int i=0;i<lamper;i++){
		bool sat=false;
		sat =((temp)&(1<<(i)));
		if (sat==false){
		return false;
		}
	


	}

	return true;
}





void read_input(){

	FILE* input_file =fopen("input.in","r");

	fscanf(input_file,"%i",&antal);
	input_array = new int* [antal];

	
	for (int i=0;i<antal;i++){
	
		input_array[i]= new int[2];
		fscanf(input_file,"%i %i",&input_array[i][0],&input_array[i][1]);

	}

}