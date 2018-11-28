#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>

using namespace std;

typedef struct _parse_elem{
		long next_pos;
		long money;
}parse_elem;


//global
long case_num  = 0;

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
		for( long case_iter = 0; case_iter < case_num ; case_iter++ ){

			//prepare
			long round;
			long capicity;
			long group_num;
			fin >> round >> capicity >> group_num ;

			//get group
			vector<long> groups;
			long reader;
			for( long i=0 ; i<group_num ; i++ ){
				fin >> reader;
				groups.push_back(reader);
			}

			//caculter list for alog
			vector<parse_elem> caculate_vector;
			parse_elem tmp;
			long cur_size;
			long next_pos;

			for( long scan_pos=0 ; scan_pos < group_num ; scan_pos++ ){
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
				cout << scan_pos << "->" << next_pos << " : " << cur_size << endl;
			}

			//caculate sum money of cur case
			long sum_money=0;
			long pos_now=0;
			long tmp_p=0;
			for( long i=0 ; i < round ; i++ ){
				sum_money += caculate_vector[pos_now].money;
				tmp_p = caculate_vector[pos_now].next_pos;
				if( tmp_p != -1 )
					pos_now = tmp_p;
			//	else
			//		pos_now = pos_now+1;
			}
			cout << "sum = " << sum_money << endl;
			cout << "---------------------" << endl;

			fout << "Case #" << case_iter+1 << ": " << sum_money << endl;
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
        parse_file("C-small-attempt0.in");
		pause();
		return 0;
}
