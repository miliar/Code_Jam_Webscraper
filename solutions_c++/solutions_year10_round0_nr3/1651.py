#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>

using namespace std;

typedef struct _parse_elem{
		long long next_pos;
		long long money;
}parse_elem;


//global
long long case_num  = 0;

//fixme
long long ring_round=0;

void pause()
{
		char s;
		cin >> s;
}

void comment(char *s)
{
		std::cout << "============================" << std::endl;
		std::cout << s << std::endl;
		std::cout << "============================" << std::endl;
}

int get_ring( vector<parse_elem> &caculate_vector)
{
	long long pos_now=0;
	long long tmp_p=0;
	int ring_pos=-1;
		
	bool do_trace=false;
	vector<int> trace;

	while(1){
		trace.push_back(pos_now);
		tmp_p = caculate_vector[pos_now].next_pos;
		cout << pos_now << "->" << tmp_p << endl;
		if( tmp_p != -1 ) {
			if( tmp_p < pos_now )//rounded pos
			{
				do_trace = true;
			}
			if( do_trace )
			{
				int i;
				for(  i = 0 ; i<trace.size() ; i++ ){
					if( tmp_p == trace[i] )
					{
						//fined ring
						//cout << "ring pos: " << tmp_p << endl;
						ring_pos=tmp_p;
						break;
					}
				}
				if( ring_pos != -1 )//we geteed ring pos now calaulte ring round
				{
					ring_round = trace.size()-i;
					break;
				}
			}
			pos_now = tmp_p;
		}
		else{//slef ring . tmp_p == -1
			ring_pos = pos_now;
			ring_round = 1;
			break;
		}
	}


	return ring_pos;
}


int parse_file(char *file_name)
{
	//open file
	fstream fin;
	fin.open(file_name,fstream::in);

	//output file
	fstream fout;
	fout.open("result.txt",fstream::out);

	//read variables
	fin >> case_num;

	//do cases
	for( long long case_iter = 0; case_iter < case_num ; case_iter++ ){

		//prepare
		long long round;
		long long capicity;
		long long group_num;
		fin >> round >> capicity >> group_num ;

		//get group
		vector<long long> groups;
		long long reader;
		for( long long i=0 ; i<group_num ; i++ ){
			fin >> reader;
			groups.push_back(reader);
		}

		//caculter list for alog
		vector<parse_elem> caculate_vector;
		parse_elem tmp;
		long long cur_size;
		long long next_pos;

		for( long long scan_pos=0 ; scan_pos < group_num ; scan_pos++ ){
			//get current group size
			cur_size = groups[scan_pos];
			next_pos = (scan_pos+1)%group_num;
			//get max size
			while( ( cur_size + groups[next_pos] ) <= capicity && next_pos!=scan_pos){
				cur_size += groups[next_pos];
				next_pos = (next_pos+1)%group_num;
			}
			if( next_pos == scan_pos )
				tmp.next_pos = -1;
			else
				tmp.next_pos = next_pos;
			tmp.money = cur_size;
			caculate_vector.push_back(tmp);
			//cout << scan_pos << "->" << next_pos << " : " << cur_size << endl;
		}

		//------------------------------------------------------
		//old caculate
		//------------------------------------------------------
		//caculate sum money of cur case
		//long long sum_money=0;
		//long long pos_now=0;
		//long long tmp_p=0;
		//for( long long i=0 ; i < round ; i++ ){
		//	sum_money += caculate_vector[pos_now].money;
		//	tmp_p = caculate_vector[pos_now].next_pos;
		//	if( tmp_p != -1 )
		//		pos_now = tmp_p;
		//}
		////cout << "sum = " << sum_money << endl;
		////cout << "---------------------" << endl;

		//fout << "Case #" << case_iter+1 << ": " << sum_money << endl;

		//------------------------------------------------------
		//new caculate
		//------------------------------------------------------
		//get ring pos
		int ring_pos = get_ring( caculate_vector );
		cout << "ring pos: " << ring_pos << endl;
		cout << "ring round: " << ring_round << endl;

		//pass one node ring
		if( ring_pos == 0 && ring_round == 1 )
		{
			cout << "self ring =" << round*caculate_vector[0].money << endl;
			fout << "Case #" << case_iter+1 << ": " << round*caculate_vector[0].money << endl;
			continue;
		}


		//caculate before ring
		int before_ring_round=0;
		int tmp_p=0;
		int pos_now=0;
		long long money_before_ring=0;
		for(  ; pos_now != ring_pos ;  ){
			money_before_ring += caculate_vector[pos_now].money;
			tmp_p = caculate_vector[pos_now].next_pos;
			before_ring_round++;
			if( tmp_p != -1 ){
				pos_now = tmp_p;
			}
			else//self round
			{
				break;
			}
		}
		cout << "money_before_ring = " << money_before_ring << "before_ring_round :" << before_ring_round << endl;

		//caculate in ring
		long long money_in_ring=0;
		pos_now = ring_pos;
		money_in_ring += caculate_vector[pos_now].money;
		tmp_p = caculate_vector[pos_now].next_pos;
		pos_now = tmp_p;
		for(  ; pos_now != ring_pos ;  ){
			money_in_ring += caculate_vector[pos_now].money;
			tmp_p = caculate_vector[pos_now].next_pos;
			if( tmp_p != -1 ){
				pos_now = tmp_p;
			}
			else//self round
			{
				break;
			}
		}

		cout << "money_in_ring = " << money_in_ring << endl;

		if( round > before_ring_round + ring_round ){

			//now ture to calaulte 
			long long round_left = ( round - before_ring_round ) % ring_round;
			long long round_ring = ( round - before_ring_round ) / ring_round;
			cout << "round_left=" << round_left << endl;

			//now calaulte money_after_ring
			long long money_after_ring=0;
			pos_now = ring_pos;
			for( int t=0 ; t < round_left ; t++ ){
				money_after_ring += caculate_vector[pos_now].money;
				tmp_p = caculate_vector[pos_now].next_pos;
				if( tmp_p != -1 ){
					pos_now = tmp_p;
				}
				else//self round
				{
					break;
				}
			}
			cout << "money_after_ring=" << money_after_ring << endl;

			long long sum_money = money_before_ring + round_ring*money_in_ring + money_after_ring;
			cout << "sum_money=" << sum_money << endl;
			fout << "Case #" << case_iter+1 << ": " << sum_money << endl;
		}
		else
		{
			//------------------------------------------------------
			//old caculate
			//------------------------------------------------------
			//caculate sum money of cur case
			long long sum_money=0;
			long long pos_now=0;
			long long tmp_p=0;
			for( long long i=0 ; i < round ; i++ ){
				sum_money += caculate_vector[pos_now].money;
				tmp_p = caculate_vector[pos_now].next_pos;
				if( tmp_p != -1 )
					pos_now = tmp_p;
			}
			cout << "sum = " << sum_money << endl;
			//cout << "---------------------" << endl;

			fout << "Case #" << case_iter+1 << ": " << sum_money << endl;
		}
	}


	//close file
	fin.close();
	fout.close();

}

int main()
{
	char s[3];
	//comment("program start!");
	//parse_file("A-small-practice.in");
	//parse_file("A-large-practice.in");
	//parse_file("C-small-attempt0.in");
	//parse_file("test.txt");
	parse_file("C-large(2).in");
	return 0;
}
