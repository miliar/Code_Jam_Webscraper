#include <iostream>


using namespace std;

void read_input();
int antal =0;
long **input_array;
long solution(int index);

FILE *ouput_file =fopen("answer.out","w");

int main(){
	
	read_input();
	for (int i=0;i<antal;i++){
		fprintf(ouput_file,"Case #%i: %d \r\n",(i+1),solution(i));
	}
    

	return 0;
}



long solution(int index){
	long length = input_array[index][2]+3;
	long passengers = input_array[index][1];
	int number_of_rides = input_array[index][0];

	long euros =0;
	int p_where=3;

	for (int i=0;i<number_of_rides;i++){
		long sum =0;
		int max_run = length-3;
		int run =0;
		for (sum=0;sum+input_array[index][p_where]<passengers+1 && run<max_run ;run++){
		sum+=input_array[index][p_where];
		p_where++;
		if (p_where>=length){
			p_where =3;
		}

		}
		euros+= sum;
	}
	return euros;

}




void read_input(){

	FILE* input_file =fopen("input.in","r");


	long R=0;
	long K=0;
	int N=0;

	fscanf(input_file,"%d",&antal);
	input_array = new long* [antal];
	for (int i=0;i<antal;i++){
		fscanf(input_file,"%i %i %i",&R,&K,&N);
		input_array[i] = new long[(N+3)];
		input_array[i][0] = R;
		input_array[i][1] = K;
		input_array[i][2] = N;
		for (int y=3;y<N+3;y++){
		
			fscanf(input_file,"%i",&input_array[i][y]);
		
		}

	}

}