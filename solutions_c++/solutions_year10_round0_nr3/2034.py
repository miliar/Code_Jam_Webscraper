#include <cstdio>
#include <iostream>
#include <fstream>
#include <list>

using namespace std;

typedef long long int t_mytype;
class Queue {
	t_mytype *groups;
	t_mytype size;
	t_mytype index;
	
	public:
		Queue(t_mytype *groups_, t_mytype size_) {
			groups = groups_;
			size = size_;
			index = -1;
		}
		
		t_mytype next() {
			index++;
			index %= size;
			return groups[index];
		}
		
		t_mytype noxt() {
			return index;
		}
		
		void goBack() {
			index--;
			index %= size;
		}
};

class Roller {	
	public:
		Queue *que;
		t_mytype euros;
		t_mytype max;
		t_mytype tot;
		
		Roller(Queue* que_, t_mytype max_, t_mytype tot_) {
			euros = 0;
			tot = tot_;
			max = max_;
			que = que_;
		}
		
		void ride(list<t_mytype>& list) {
			t_mytype inside = 0;
			t_mytype groups = 0;
			t_mytype last = 0;
			t_mytype lest = 0;
			
			while( inside <= max && groups <= tot ) {
				if( last != 0 )
					list.push_back(lest);
				last = que->next();
				lest = que->noxt();
				inside += last;
				groups++;
			}
			
			inside -= last;
			que->goBack();
			
			euros += inside;

		}
};

int main() {
	ifstream in;
	in.open("C-large.in");
	ofstream out;
	out.open("C-large.out");
	
	t_mytype t;
	in >> t;
	
	for(t_mytype i = 1; i <= t; i++) {
		t_mytype  r, k, n;
		in >> r; in >> k; in >> n;
		
		t_mytype *quearray = new t_mytype[n];
		
		for(t_mytype j = 0; j < n; j++) {
			t_mytype tmp;
			in >> tmp;
			quearray[j] = tmp;
		}
		
		Queue *que = new Queue(quearray, n);
		Roller *roller = new Roller(que, k, n);
		list< list<t_mytype> > insiden;
		t_mytype sums = 0;
		
		for(int j = 0; j < r; j++) {
			
			list<t_mytype> lista;
			roller->ride(lista);
			
			bool flag = false;
			list<list<t_mytype> > loopList;
			
			list<list<t_mytype> >::iterator it = insiden.begin();
			
			for (; it != insiden.end(); it++) {
				if( *it == lista ) 
						flag = true;	
				if(flag) {
					loopList.push_back(*it);
				}
			}
			
			insiden.push_back(lista);
			
			t_mytype sum = 0;
			
			if(flag) {
				for(list<list<t_mytype> >::iterator it = loopList.begin();
					it != loopList.end(); it++)
					for(list<t_mytype>::iterator is = it->begin();
					is != it->end(); is++)
						sum += quearray[*is];
			}
			
			if(flag) {			
				sums += ((t_mytype) ((r-j-1)/loopList.size()))*sum;
				j = j + ((t_mytype) ((r-j-1)/loopList.size()))*loopList.size();
				loopList.clear();
			}

		}
		
		out << "Case #" << i << ": " << sums + roller->euros << endl;
		cout << "Case #" << i << ": " << sums + roller->euros << endl;
	}
	
}
