#include <vector>
#include <iostream>

using namespace std;

struct item
{
    long num;

    long sum;
    int next;

    long long at_step;
    long long sum_was;
    long long sum_per_cycle;
    long long steps_in_cycle;
};

void solve()
{
	long long R, k;
	long N;
	cin >> R >> k >> N;
	vector<item> v = vector<item>(N);
	for(int i=0;i<N;++i) {
	    cin>>v[i].num;
    }
	for(int i=0;i<N;++i) {
	    long long ksum = v[i].num;
	    int next = (i+1)%N;
        for(int j=1;j<N;++j) {
            if(ksum + v[next].num > k) {
                break;
            }
            ksum += v[next].num;
            next = (next+1)%N;
        }
        v[i].sum = ksum;
        v[i].next = next;

        v[i].at_step = -1;
        v[i].sum_was = -1;
        v[i].sum_per_cycle = -1;
        v[i].steps_in_cycle = -1;
    }

    long long sum = 0;
    int pos = 0;
	for(int i=0;i<R;++i) {
	    if(v[pos].steps_in_cycle == -1) {
            if(v[pos].at_step == -1) {
                v[pos].at_step = i;
                v[pos].sum_was = sum;
            } else {
                v[pos].sum_per_cycle = sum - v[pos].sum_was;
                v[pos].steps_in_cycle = i - v[pos].at_step;
            }
	    }

	    if(v[pos].steps_in_cycle != -1 && v[pos].steps_in_cycle < R-i) {
	        long long big_cycles = (R-i)/v[pos].steps_in_cycle;
	        sum += (v[pos].sum_per_cycle * big_cycles);
	        i += ((v[pos].steps_in_cycle * big_cycles) - 1);
            /*
	        sum += v[pos].sum_per_cycle;
	        i += v[pos].steps_in_cycle - 1;
	        */
	        continue;
	    }
	    else
        {
        sum += v[pos].sum;
        pos = v[pos].next;
        }
	}

	cout << sum << endl;
}


int main(int argc, char* argv[])
{
	int T;
	cin >> T;
	for( int i = 0; i < T; ++i ) {
                cout << "Case #" << i+1 << ": ";
                solve();
	}
	return 0;
}
//---------------------------------------------------------------------------
