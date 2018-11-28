#include <stdio.h>
#include <set>
using namespace std;
const int DEPARTS=0;
const int GET_READY=1;

struct Event
   {
	   int station, type, time, id;
		Event(int _id)
		   {
			   station=0;
				type=DEPARTS;
				time=0;
				id=_id;
			}
	};
	
bool operator <(const Event &A, const Event &B)
   {
	   if(A.time==B.time)
		   {
			   if(A.type==B.type)
			      return A.id<B.id;
				else
				   return A.type==GET_READY;
			}
	   return A.time<B.time;
	}

int format(char *buffer)
   {
	   return ((buffer[0]-'0')*10+(buffer[1]-'0'))*60+((buffer[3]-'0')*10+(buffer[4]-'0'));
	}
char buffer[50];
int main()
   {
	   int N;
		scanf("%d", &N);
		for(int caso=1;caso<=N;caso++)
		   {
			   int T, na, nb;
				scanf("%d%d%d", &T, &na, &nb);
				set<Event> events;
				for(int i=0;i<na+nb;i++)
				   {
					   Event e0(2*i);
						e0.station=(i<na)?0:1;
					   scanf("%s",buffer);
						e0.time=format(buffer);
						e0.type=DEPARTS;
						events.insert(e0);
						
						Event e1(2*i+1);
						e1.station=1-e0.station;
						scanf("%s",buffer);
						e1.time=format(buffer)+T;
						e1.type=GET_READY;
						events.insert(e1);
					}
				int count[2];
				int needed[2];
				count[0]=count[1]=0;
				needed[0]=needed[1]=0;
				while(!events.empty())
				   {
					   Event actual=*events.begin();
						//printf("%d %d %d\n",actual.time, actual.type, actual.station);
						events.erase(events.begin());
						if(actual.type==DEPARTS)
						   {
							   if(count[actual.station]==0)
							      needed[actual.station]++;
								else
									count[actual.station]--;
							}
						else
					      count[actual.station]++;
					}
				printf("Case #%d: %d %d",caso, needed[0], needed[1]);
				if(caso<N)
				   printf("\n");
			}
	   return 0;
	}
