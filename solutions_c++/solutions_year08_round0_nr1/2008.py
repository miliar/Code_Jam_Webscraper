#include<iostream>
#include<cstring>
#include<map>
#include<vector>
using namespace std;

struct strCmp{
	bool operator()(const char*a, const char*b){
		return strcmp(a, b) < 0 ;
	}
};

struct seg{
	int value, pre, first, last, end;
};

map<char*, int, strCmp> list;
void segment(vector<int> & queries, int first, int end, seg & status){
	if(end-first == 0){
		if(status.pre == status.end || status.pre == -1 || status.end == -1)
			status.value = 0;
		else
			status.value = 1;
		return;
	}
	if(end-first == 1){
		if(status.pre == -1 && status.end == -1){
			status.first = status.last = (queries[first] +1) % list.size();
			status.value = 0;
		}else if(status.pre == -1 || status.end == -1){
			if( queries[first] == status.end || queries[first] == status.pre){
				status.first = status.last = ( queries[first] +1) % list.size();
				status.value = 1;
			}else{
				status.first = status.last = (status.end == -1 ? status.pre : status.end);
				status.value = 0;
			}
		}else if(status.pre == queries[first] ){
			for(int k = 0 ; k < list.size() ; k++)
				if(k != status.pre && (status.pre == status.end || k == status.end)){
					status.first = status.last = k;
					break;
				}
			if(status.pre == status.end)
				status.value = 2;
			else
				status.value = 1;
		}else{
			status.first = status.last = status.pre;
			if(status.pre == status.end)
				status.value = 0;
			else
				status.value = 1;
		}
#ifdef DEBUG
		cout << "\t\tSeg \t[" << status.pre << "]"  << first << "(" << status.first << ")\t--\t" << end-1 << "(" << status.last << ")[" << status.end << "]" << " / " << queries.size() << " :: " << status.value << endl;
#endif
		return;
	}
	int mid = (first+end)/2, type = list.size();
	seg tmp1 = status, tmp2 = status, min = status;
	min.value = end-first+10;
	for(int i = 0, k ; i < type ; i++ ){
		if(i == queries[mid] )
			continue;
		tmp1.end = tmp2.pre = i;
		for(k = mid+1 ; k < end && queries[k] != i ; k++);
		segment(queries, first, mid, tmp1);
		segment(queries, k, end, tmp2);
		if(tmp1.value + tmp2.value < min.value){
			min.first = tmp1.first;
			min.last = tmp2.last;
			min.value = tmp1.value + tmp2.value;
		}
#ifdef DEBUG
		cout << "\tvalue:" << tmp1.value + tmp2.value << "\t" << first << "'" << queries[first] << "'[" << tmp1.first << "](" << queries[first] << ")," << mid << "'" << queries[mid] << "'[" << i << "](" << queries[mid] << "),'" << queries[end-1] << "'" << end-1 << "[" << tmp2.last << "](" << queries[end-1]<< ")" << endl;
#endif
	}
#ifdef DEBUG
	cout << "Seg \t[" << status.pre << "]"  << first << "\t--\t" << end-1  << "[" << status.end << "]" << " / " << queries.size() << endl;
#endif
	status = min;
}

int main(){
	int N, S, Q;
	char str[200];
	vector<int> queries;
	seg status;
	cin >> N;
	for(int i = 0 ; i < N ; i++){
		cin >> S;
		cin.ignore(100, '\n');
		for(int j = 0 ; j < S ; j++){
			cin.getline(str, 199);
			list[strdup(str)] = j;
		}
		cin >> Q;
		cin.ignore(100, '\n');
		for(int j = 0 ; j < Q ; j++){
			cin.getline(str, 199);
			queries.push_back(list[str]);
		}
		status.pre = status.end = -1;
		segment(queries, 0, Q, status);
		list.clear();
		queries.clear();
		cout << "Case #" << i+1 << ": "<< status.value << endl;
	}
}
