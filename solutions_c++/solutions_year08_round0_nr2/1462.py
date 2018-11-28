#include <set>
#include <iostream>
#include <string>
//#define DEBUG

class time_class{
	public:
		int hour, minute;
		time_class():hour(0),minute(0){};
		time_class(std::string time_class_);
		const time_class operator-(int i) const;
};
time_class::time_class(std::string time_class_){
	hour = (time_class_[0] - '0')*10 + (time_class_[1] - '0');
	minute = (time_class_[3] - '0')*10 + (time_class_[4] - '0');
}

const time_class time_class::operator- (int i) const{
	time_class t;
	t.minute = minute -  i;
	t.hour = hour;
	if (t.minute < 0){
		while(t.minute < 0)
			t.minute += 60;
		--t.hour;
	}
	return t;
}

struct comptime_class {
	bool operator() (const time_class& lhs, const time_class& rhs) {
		if(lhs.hour != rhs.hour) return (lhs.hour < rhs.hour);
		else return (lhs.minute < rhs.minute);
	}
};

int main(){
	int N;
	std::cin >> N;
	for (int cases = 1; cases <= N; ++cases){
		int T, NA, NB;
		std::cin >> T >> NA >> NB;
		#ifdef DEBUG
			std::cout<<T<<" "<<NA<<" "<<NB<<std::endl;
		#endif
		//strings are already going to be enough to compare with, since they're already going
		//to have the same order as if we used a time class!
		std::pair<std::multiset<time_class, comptime_class>, std::multiset<time_class, comptime_class> > A_to_B_timetable, B_to_A_timetable;
		//for each trip from A to B, record the times
		for(int A_to_B_trips = 1; A_to_B_trips <= NA; ++A_to_B_trips){
			std::string start, end;
			std::cin >> start >> end;
			A_to_B_timetable.first.insert(time_class(start));
			A_to_B_timetable.second.insert(time_class(end));
			#ifdef DEBUG
				std::cout<<start.size()<<std::endl;
				std::cout <<time_class(start).hour<<":"<<time_class(start).minute<<std::endl;
				std::cout<<end.size()<<std::endl;
				std::cout<<time_class(end).hour<<":"<<time_class(end).minute<<std::endl;
			#endif
		}
		//then do the same for trips from B to A
		for(int B_to_A_trips = 1; B_to_A_trips <= NB; ++B_to_A_trips){
			std::string start, end;
			std::cin >> start >> end;
			B_to_A_timetable.first.insert(time_class(start));
			B_to_A_timetable.second.insert(time_class(end));
		}
		//now look at whether we need more trains or not
		int extra_trains_at_A = 0;
		for(std::multiset<time_class, comptime_class>::iterator from_A = A_to_B_timetable.first.begin();
												from_A != A_to_B_timetable.first.end();
												++from_A)
		{
			std::multiset<time_class, comptime_class>::iterator to_A = B_to_A_timetable.second.upper_bound(*from_A - T);
			if(to_A != B_to_A_timetable.second.begin()){
				--to_A;
				B_to_A_timetable.second.erase(to_A);
			}
			else{
				++extra_trains_at_A;
			}
		}
		// and do the same for extra trains at B
		int extra_trains_at_B = 0;
		for(std::multiset<time_class, comptime_class>::iterator from_B = B_to_A_timetable.first.begin();
												from_B != B_to_A_timetable.first.end();
												++from_B)
		{
			std::multiset<time_class, comptime_class>::iterator to_B = A_to_B_timetable.second.upper_bound(*from_B - T);
			if(to_B != A_to_B_timetable.second.begin()){
				--to_B;
				A_to_B_timetable.second.erase(to_B);
			}
			else{
				++extra_trains_at_B;
			}
		}
		//finally, print out solution
		std::cout << "Case #" << cases << ": " << extra_trains_at_A << " " << extra_trains_at_B << std::endl;
	}
	return 0;
}

