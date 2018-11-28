#include <cstdio>
#include <queue>

using namespace std;

class event
{
	public:
		int tt; // time
		bool station; // 0 = A, 1 = B
		int type; // 0 = arrive,wait = 1,dep = 2;

		bool operator<(event const &right) const
		{
			if(tt > right.tt) return true;
			if(right.tt > tt) return false;
			if(type < right.type) return false;
			return true;
		}
};

int main()
{
	int N,T,na,nb,wa,wb,ma,mb;
	event e,f;
	char ch[15];
	scanf("%d\n",&N);

	priority_queue<event> Q;
	for(int nn = 1;nn <= N; ++nn) {
		ma = mb = wa = wb = 0;
		scanf("%d\n%d %d\n",&T,&na,&nb);
		for(int i=0;i<na;++i) {
			scanf("%s ",ch);
			e.tt  = (((int)ch[0]-48)*10 + (int)ch[1] - 48)*60 + ((int)ch[3] - 48)*10 + (int)ch[4] - 48;
			e.station = 0;
			e.type = 2;
			Q.push(e);

			scanf("%s\n",ch);
			e.tt =  (((int)ch[0]-48)*10 + (int)ch[1] - 48)*60 + ((int)ch[3] - 48)*10 + (int)ch[4] - 48;
			e.station = 1;
			e.type = 0;
			Q.push(e);

			//fprintf(stderr,"%d %d\n",depA[i],arrA[i]);
		}
		for(int i=0;i<nb;++i) {
			scanf("%s ",ch);
			e.tt  = (((int)ch[0]-48)*10 + (int)ch[1] - 48)*60 + ((int)ch[3] - 48)*10 + (int)ch[4] - 48;
			e.station = 1;
			e.type = 2;
			Q.push(e);

			scanf("%s\n",ch);
			e.tt  = (((int)ch[0]-48)*10 + (int)ch[1] - 48)*60 + ((int)ch[3] - 48)*10 + (int)ch[4] - 48;
			e.station = 0;
			e.type = 0;
			Q.push(e);

			//fprintf(stderr,"%d %d\n",depB[i],arrB[i]);
		}
		while(!Q.empty()) {
			e = Q.top();
			//fprintf(stderr,"%d %s %s \n",e.tt,(e.station == 1) ? "B" : "A",(e.type == 1) ? "turn" : (e.type == 0) ? "arrival" : "departure");
			switch(e.type) {
				case 0:
					// arrival
					f.tt  = e.tt + T;
					f.type = 1;
					f.station = e.station;
					Q.pop();
					Q.push(f);
					break;
				case 1:
					if(e.station == 0) wa++;
					else wb++;
					Q.pop();
					// end of turn around
					break;
				case 2:
					// departure
					if(e.station == 0) {
						if(wa > 0) wa--;
						else ma++;
					}
					else {
						if(wb > 0) wb--;
						else mb++;
					}
					Q.pop();
					break;
				default:
					fprintf(stderr,"Why am I here\n");
					break;
			}
		}
		printf("Case #%d: %d %d\n",nn,ma,mb);
	}
	return 0;
}
