
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <set>

struct time_tableT {
	int station;
	int time1;
	int time2;
};

struct time_table_less {
	int operator()(const time_tableT& left, const time_tableT& right) const {
		if(left.time1<right.time1){
			return true;
		}
		if(left.time1==right.time1){
			if(left.time2<right.time2){
				return true;
			}
			if(left.time2==right.time2){
				return left.station<right.station;
			}
		}

		return false;
	}
};

std::multiset<int>::iterator Find(std::multiset<int>& buf, int tmm){
	for(std::multiset<int>::iterator i=buf.begin();
		i!=buf.end();
		++i)
	{
		if(*i <= tmm){
			return i;
		}
	}

	return buf.end();
}

int Handle(int cur_task, int turn_time, std::vector<time_tableT>& tt ){

	// trains at moments
	typedef std::multiset<int> TrainsT;
	TrainsT atA;
	TrainsT atB;

	std::cerr<<"turn time "<<turn_time<<std::endl;

	int trainsA=0;
	int trainsB=0;

	for(std::vector<time_tableT>::iterator i=tt.begin();
		i!=tt.end();
		++i)
	{
		if(i->station==0){	// A
			std::cerr<<"from A at "<<i->time1/60<<":"<<i->time1%60<<std::endl;
			TrainsT::iterator tr=Find(atA,i->time1);
			if( atA.end()==tr ){
				std::cerr<<"added train from A"<<std::endl;
				trainsA++;
			}else{
				std::cerr<<"moved train from A ("<<*tr/60<<":"<<*tr%60<<")"<<std::endl;
				atA.erase(tr);
			}
			atB.insert( i->time2+turn_time );
		}
		if(i->station==1){	// B
			std::cerr<<"from B at "<<i->time1/60<<":"<<i->time1%60<<std::endl;
			TrainsT::iterator tr=Find(atB, i->time1);
			if( atB.end()==tr ){
				std::cerr<<"added train from B"<<std::endl;
				trainsB++;
			}else{
				std::cerr<<"moved train from B ("<<*tr/60<<":"<<*tr%60<<")"<<std::endl;
				atB.erase(tr);
			}
			atA.insert( i->time2+turn_time );
		}

	}

	std::cerr<<"Case #"<<cur_task+1<<": ";
	std::cerr<<trainsA<<" "<<trainsB;
	std::cerr<<std::endl;

	//return 0;
}

int main(void){

	//const std::string fname="in1";
	//const std::string fname="A-small-attempt1.in";
	//const std::string fname="A-small-attempt2.in";
	//const std::string fname="in2";
	const std::string fname="B-large.in";
	std::ifstream rd;
	rd.open(fname.c_str());

	int task_count=0;
	rd>>task_count;
	std::cerr<<"task count "<<task_count<<std::endl;

	for(int cur_task=0; cur_task<task_count; cur_task++){

		int turn_time=0;
		rd >> turn_time;

		int a2b=0;
		rd >> a2b;
		int b2a;
		rd >> b2a;

		std::vector<time_tableT> time_table;

		for(int i=0; i<a2b+b2a ; i++){
			int h1=0;
			int m1=0;
			int h2=0;
			int m2=0;

			char unu;
			rd >> h1; rd.get(unu);
			rd >> m1;
			rd >> h2; rd.get(unu);
			rd >> m2;

			std::cerr<<"["<<h1<<":"<<m1<<"] ["<<h2<<":"<<m2<<"]"<<std::endl;

			int ttm1=(h1*60)+m1;
			int ttm2=(h2*60)+m2;

			time_tableT tmp;
			tmp.station=i<a2b?0:1; // 0 - A; 1 - B
			tmp.time1=ttm1;
			tmp.time2=ttm2;
			time_table.push_back(tmp);

		}

		std::sort( time_table.begin(), time_table.end(), time_table_less() );

		Handle(cur_task, turn_time, time_table);

	}

	return 0;

}




