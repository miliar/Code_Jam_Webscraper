#include <iostream>
#include <cstdlib>

using namespace std;

int main(int argc, char *argv[])
{
    int n, num, step, ostep, bstep, index, count;
    char ch, prech;
    int prestep;
    cin >> n;
    int times = 0;
    while(times++ < n){
	cin >> num;
	ostep = bstep = 1;
	count = prestep = prech = 0;
	while(num-- > 0){
	    cin >> ch >> step;
	    if(ch == 'O'){
		if(prech == ch){
		    count += abs(step - ostep)+1;
		    prestep += abs(step - ostep)+1;
		}else{
		    prestep = (abs(step - ostep) - prestep > 0 ? (abs(step - ostep) - prestep):0) + 1;
		    count += prestep;
		    prech = ch;
		}
		ostep = step;
	    }else if(ch == 'B'){
		if(prech == ch){
		    count += abs(step - bstep)+1;
		    prestep += abs(step - bstep)+1;
		}else{
		    prestep = (abs(step - bstep) - prestep > 0 ? (abs(step - bstep) - prestep):0) + 1;
		    count += prestep;
		    prech = ch;
		}
		bstep = step;
	    }
	}

	cout << "Case #" << times << ": " << count << endl;
    }
    return 0;
}
