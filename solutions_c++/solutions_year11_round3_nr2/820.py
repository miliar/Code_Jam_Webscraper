#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;

int main(int artc, char* argv[]) {

    int TIME;// number of test
    cin >> TIME;
    long long int L,t,N,C;
    long long int dis[1000];
    long long int ans;
    long long int dis_sum;
    long long int total_dis[1000];
    for (int tt = 0 ; tt < TIME; tt++) {
	dis_sum = 0;
	cin >> L >> t >> N >> C;
	for (int i = 0 ; i < C; ++i) {
	    cin >> dis[i];
	    total_dis[i] = dis_sum;
	    dis_sum +=dis[i];
	}
	long long int remain;
	long long int turn;
	long long int eindex;
	long long int times;
	long long int left_time;
	long long int list[1000001];
	int count;
	long long int save;
	turn = dis_sum * (N/C) + total_dis[N%C];
//	cout <<"turn " << turn << endl;
	if (t > turn * 2) ans = turn * 2;
	else {
	    remain = t % (2 * dis_sum);
	    times = t / (dis_sum * 2);
	    for (int i = C -1 ; i >= 0; --i ) {
		if (remain >= total_dis[i] * 2) {
		    eindex = i ;
		    left_time = remain - total_dis[i];
		    break;
		}
	    }
//	    cout << "times " << times << endl;
//	    cout << "eindex " <<eindex << endl;
	    count = 0;
	    for (int i = times * C + eindex + 1; i < N; ++i ) {
		list[count] = dis[i%C];
		//cout << "i,dis " << i << " " <<dis[i%C] << endl;
		count++;
	    }
	    list[count] = (( total_dis[eindex] + dis[eindex]) * 2 -remain) / 2;
//	    cout << remain << " " << list[count]<< " "<< endl;
//	    cout << "list " << list[count] << endl;
//	    for (int i = 0 ;i < count+1; ++i) cout <<list[i] << endl;
	    sort(list,list+count+1);
//	    for (int i = 0 ;i < count+1; ++i) cout <<list[i] << endl;
//	    cout << endl;
	    save = 0;
	    for (int i = 0 ; i < L ; ++i) {
		save += list[count  -i];
//		cout << save << endl;
	    }
	    ans = turn * 2 - save;
	}

	//output
	printf("Case #%d: %lld\n",tt+1, ans);
    }
    return 0;
}
