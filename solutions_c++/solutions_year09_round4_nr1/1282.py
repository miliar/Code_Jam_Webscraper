#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <boost/shared_ptr.hpp>
#include <deque>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long Int;

template <class T>
void print(const T& c)
{
	typedef typename T::const_iterator const_iterator; 
	const_iterator i;
	for(i=c.begin();i!=c.end();i++){
		cout << *i << " ";
	}
	cout << endl;
}

template <class T>
ostream& operator<<(ostream& os, const vector<T>& c)
{
	typedef typename vector<T>::const_iterator const_iterator; 
	const_iterator i;
	for(i=c.begin();i!=c.end();i++){
		os << *i << " ";
	}
	os << endl;
	return os;
}

//typedef pair<VI,int> State;
typedef pair<int,int> State;
int N;

int set(int& n, int k, int v)
{
	int f = 7;
	f = f << (3*k);
	n &= (~f);
	n |= ((v&7) << (3*k));
}

int get(int n, int k)
{
	n = n >> (3*k);
	return n&7;
}

bool ok(State& s)
{
	//VI& vi = s.first;
	int vi = s.first;
	for(int i=0;i<N;i++){
		//if( vi[i] > i )return false;
		if( get(vi,i) > i )return false;
	}
	return true;
}

bool exists(deque<State>& que, State& s)
{
	deque<State>::iterator i;
	for(i=que.begin();i!=que.end();i++){
		if( i->first == s.first ){
			return i->second <= s.second;
		}
	}
	return false;
}

void put(int i)
{
	for(int j=0;j<N;j++){
		cout << get(i,j) << " ";
	}
	cout << endl;
}

		
int main(int argc, char *argv[])
{
	int T;
	cin >> T;
	for(int i=0;i<T;i++){
		//cout << "start Case #" << i << ": " << endl;
		cin >> N;
		//cout << N << endl;
		//VI v(N);
		int v = 0;
		for(int j=0;j<N;j++){
			string s;
			cin >> s;
			for(int k=0;k<N;k++){
				if( s[k] == '1' ){
					set(v,j,k);
					//v[j] = k;
					// cout << "verify: " << k << " " << get(v,j) << endl;
				}
			}
		}

		deque<State> que, reached;
		que.push_back( State(v,0) );

		while( !que.empty() ){
			State s = que.front();
			//cout << "vi: " << s.first << endl;
			que.pop_front();
			if( ok(s) ){
				cout << "Case #" << (i+1) << ": " << s.second << endl;
				break;
			}
			
			reached.push_back( s );
			for(int r=0;r<N-1;r++){
				//VI newvi = s.first;
				int newvi = s.first;

				//put(newvi);
				//cout << "change " << r << " " << (r+1) << endl;
				int tmp = get(newvi,r);
				int v = get(newvi,r+1);
				set(newvi,r,v);
				set(newvi,r+1,tmp);
				//put(newvi);
				// swap(newvi[r],newvi[r+1]);
				State ns(newvi,s.second+1);
				if( !exists(que, ns) && !exists(reached, ns) ){
					que.push_back( ns );
				}
			}
		}
		// cout << ans << endl;
	}
	
    return 0;
}



