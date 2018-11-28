
#include <iostream>
#include <vector>

using namespace std;

enum color
{
	Undefined,
	O, 
	B
};

struct task
{
	task()
		: cl( color::Undefined ), pos( 0 ) {}

	task( color cl_, int pos_ )
		: cl( cl_ ), pos( pos_ ) {}

	color cl;
	int pos;
};

int solve( const vector<task>& ts )
{
	int n = ts.size();
	int time = 0;
	int done_tasks = 0;
	int o_pos = 1, b_pos = 1;
	while ( done_tasks < n ) {
		color curr_cl, next_cl;
		if ( ts[ done_tasks ].cl == color::O ) {
			curr_cl = color::O;
			next_cl = color::B;
		}
		else if ( ts[ done_tasks ].cl == color::B ) {
			curr_cl = color::B;
			next_cl = color::O;
		}

		int next_o_pos = 0, next_b_pos = 0;
		for ( int i = done_tasks; i < n; ++i )
			if ( ts[ i ].cl == color::O ) {
				next_o_pos = ts[ i ].pos;
				break;
			}
		for ( int i = done_tasks; i < n; ++i )
			if ( ts[ i ].cl == color::B ) {
				next_b_pos = ts[ i ].pos;
				break;
			}
		int o_step = 0, b_step = 0;
		int o_next_dist = abs( o_pos - next_o_pos );
		int b_next_dist = abs( b_pos - next_b_pos );
		if ( next_o_pos != 0 ) {
			if ( o_pos < next_o_pos ) o_step = 1;
			else if ( o_pos > next_o_pos ) o_step = -1;
		}
		if ( next_b_pos != 0 ) {
			if ( b_pos < next_b_pos ) b_step = 1;
			else if ( b_pos > next_b_pos ) b_step = -1;
		}

		if ( ts[ done_tasks ].cl == color::O ) {
			o_pos += o_step * o_next_dist;
			if ( o_next_dist <= b_next_dist )
				b_pos += b_step * o_next_dist;
			else
				b_pos = next_b_pos;
			time += o_next_dist;
			++done_tasks;
			if ( b_pos != next_b_pos )
				b_pos += b_step;
			++time;
		}
		else if ( ts[ done_tasks ].cl == color::B ) {
			b_pos += b_step * b_next_dist;
			if ( b_next_dist <= o_next_dist )
				o_pos += o_step * b_next_dist;
			else
				o_pos = next_o_pos;
			time += b_next_dist;
			++done_tasks;
			if ( o_pos != next_o_pos )
				o_pos += o_step;
			++time;
		}
	}
	return time;
}

int main()
{
	int TC;
	cin >> TC;
	for ( int tc = 1; tc <= TC; ++tc ) {
		int n;
		cin >> n;
		cerr << "test " << tc << ": n = " << n << endl;
		vector<task> ts;
		ts.reserve( n );
		for ( int i = 0; i < n; ++i ) {
			task t;
			char ch;
			cin >> ch;
			if ( ch == 'O' )
				t.cl = color::O;
			else if ( ch == 'B' )
				t.cl = color::B;
			cin >> t.pos;
			ts.push_back( t );
		}
		int r = solve( ts );
		cout << "Case #" << tc << ": " << r << endl;
	}
	return 0;
}
