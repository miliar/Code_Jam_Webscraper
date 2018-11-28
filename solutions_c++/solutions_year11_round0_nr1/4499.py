#include <iostream>
#include <limits>
using namespace std;

char * small_in = "A-small-practice.in";
char * small_out = "A-small-practice.out";
char * small_att_in =  "A-small-attempt1.in";
char * small_att_out = "A-small-attempt1.out";
char * large_in = "A-large.in";
char * large_out = "A-large.out";

const int MAX_SEQ_LEN = 100;

int Abs ( int x )
{
	if ( x < 0 ) return -x;
	else return x;
}

int main()
{
	freopen(large_in, "rt", stdin);
	freopen(large_out, "w", stdout);

	int T;
	cin >> T;

	for ( int i = 0; i < T; i++ )
	{
		// Case i
		char seq_who[MAX_SEQ_LEN];
		int seq_where[MAX_SEQ_LEN];

		int orange_seq[MAX_SEQ_LEN];
		int blue_seq[MAX_SEQ_LEN];

		int OrangeWaitWhileBlue[MAX_SEQ_LEN];
		int BlueWaitWhileOrange[MAX_SEQ_LEN];

		int orange_count = 0;
		int blue_count = 0;

		int N = 0;
		cin >> N;

		for ( int j = 0; j < N; j++ )
		{
			char who;
			int at;
			cin >> who;
			cin >> at;

			seq_who[j] = who;
			seq_where[j] = at;
		}

		int orangePos = 1;
		int bluePos = 1;

		int orangeDelta = 0;
		int blueDelta = 0;

		int fullTime = 0;

		for ( int j = 0; j < N; j++ )
		{
			if ( seq_who[j] == 'O' )
			{
				int spentTime = Abs( orangePos - seq_where[j] );
				fullTime += (spentTime < blueDelta)?0:(spentTime - blueDelta);
				fullTime += 1;
				orangeDelta += ((spentTime < blueDelta)?0:(spentTime - blueDelta)) + 1;
				blueDelta = 0;
				orangePos = seq_where[j];
			}
			else if ( seq_who[j] == 'B' )
			{
				int spentTime = Abs( bluePos - seq_where[j] );
				fullTime += (spentTime < orangeDelta)?0:(spentTime - orangeDelta);
				fullTime += 1;
				blueDelta += ((spentTime < orangeDelta)?0:(spentTime - orangeDelta)) + 1;
				orangeDelta = 0;
				bluePos = seq_where[j];
			}
			
		}
		cout << "Case #" << i+1<<": "<<fullTime<<endl;
	}

	return 0;
}