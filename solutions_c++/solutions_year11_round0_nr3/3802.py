/*
 * main.cpp
 *
 *  Created on: May 7, 2011
 *      Author: stefan
 */

#include <iostream>
#include <fstream>

using namespace std;

//#define DEBUG 1

unsigned long sum(unsigned long a, unsigned long b){
	unsigned long result = 0;

	for(size_t i = 0; i < sizeof(unsigned long) * 8; i++)
		result = result | (((((1<<i) & a) >> i) ^ (((1<<i) & b) >> i)) << i);

	return result;
}

#ifdef DEBUG

void print_solution(char* assignment, int N){
	for(int i = 0; i < N; i++){
		cout<<assignment[i]<<" ";
	}
	cout<<endl;
}

#endif

unsigned long sum(size_t* values, size_t N, char* assignment){
	unsigned long s = 0;
	for(size_t i = 0; i < N; i++)
		if(assignment[i] == 'S')
			s+=values[i];

	return s;
}

void separate(
		size_t* values, size_t N,
		char* assignment,
		size_t current_index,
		unsigned long current_sum_sean, unsigned long current_sum_patrick,
		bool sean_set_valid, bool patrick_set_valid,
		unsigned long& max_sum_sean){
	if(current_index == N){
		if(sean_set_valid && patrick_set_valid){
			unsigned long s = sum(values, N, assignment);
			if((current_sum_sean == current_sum_patrick) && (max_sum_sean <= s)){
				max_sum_sean = s;

#ifdef DEBUG
			print_solution(assignment, N);
			cout<<"\t"<<current_sum_sean<<" "<<current_sum_patrick<<endl;
			cout<<"\t"<<s<<endl;
#endif
			}
		}
	}
	else{
		assignment[current_index] = 'S';
		unsigned long temp;
		temp = current_sum_sean;
		current_sum_sean = sum(current_sum_sean, values[current_index]);
		separate(
				values, N,
				assignment,
				current_index+1,
				current_sum_sean, current_sum_patrick,
				true, patrick_set_valid,
				max_sum_sean);
		current_sum_sean = temp;

		assignment[current_index] = 'P';
		temp = current_sum_patrick;
		current_sum_patrick = sum(current_sum_patrick, values[current_index]);
		separate(
				values, N,
				assignment,
				current_index+1,
				current_sum_sean, current_sum_patrick,
				sean_set_valid, true,
				max_sum_sean);
		current_sum_patrick = temp;
	}
}

int main(){
	ifstream in("input.txt");
	ofstream out("output.txt");

	int T;
	in>>T;
	for(int round = 1; round <= T; round++){
		size_t N;
		in>>N;

		size_t values[N];

		for(size_t i = 0; i < N; i++){
			in>>values[i];
		}

		char assignment[N];
		unsigned long max_sum_sean = 0;
		separate(values, N, assignment, 0, 0, 0, false, false, max_sum_sean);

		out<<"Case #"<<round<<": ";
		if(max_sum_sean == 0)
			out<<"NO";
		else
			out<<max_sum_sean;
		out<<endl;

#ifdef DEBUG
		getchar();
#endif
	}

	out.close();
	in.close();

	return 0;
}
