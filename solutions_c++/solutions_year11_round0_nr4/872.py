#include <iostream>
#include <fstream>
#include <string>
#include <vector>
/*class bignum{
public:
	std::vector<unsigned short> vals;
	bignum(){}
	bignum(unsigned short val){
		vals.push_back(val);
	}
	bignum operator*(bignum b){
		bignum r;
		r.vals = std::vector<unsigned short>(vals.size()+b.vals.size(),0);
		for(int i = 0;i < vals.size();i++){
			for(int j = 0;j < b.vals.size();j++){
				int x = ((int)vals[i])*b.vals[j];
				unsigned short big = x >> 16;
				unsigned short small = x % 65536;
				r.vals[i+j] += small;
				r.vals[i+j+1] += big;
			}
		}
		return r;
	}
	bignum operator+(bignum b){
		if(vals.size() < b.vals.size()) return b + *this;
		bignum r;
		r.vals = std::vector<unsigned short>(vals);
		int i = 0;
		for(;i < b.vals.size();i++){
			r.vals[i] += b.vals[i];
		}
	}
	bool operator==(short b){
		return (vals.size() == 1 && vals[0] == b);
	}
	bool operator==(bignum b){
		if(vals.size() == b.vals.size()) return false;
		for(int i = 0;i < vals.size();i++){
			if(vals[i] != b.vals[i]) return false;
		}
		return true;
	}
	bool operator!=(short b){
		return (vals.size() != 1 || vals[0] != b);
	}
	bool operator!=(bignum b){
		if(vals.size() == b.vals.size()) return true;
		for(int i = 0;i < vals.size();i++){
			if(vals[i] != b.vals[i]) return true;
		}
		return false;
	}
	short mod2(){
		return vals[0]%2;
	}
	void lshift(){
		bool carry = false;
		for(int i = 0;i < vals.size();i++){
			bool nextcarry = (vals[i] >= 32768);
			vals[i] = vals[i] << 1;
			if(carry){
				vals[i] += 1;
			}
		}
		if(carry){
			vals.push_back(1);
		}
	}
	void rshift(){
		bool carry = false;
		if(vals[vals.size()-1] == 1){
			carry = true;
			vals.pop_back();
		}
		for(int i = vals.size()-1;i >= 0;i--){
			bool nextcarry = (vals[i]%2 == 1);
			vals[i] = vals[i] >> 1;
			if(carry){
				vals[i] += 32768;
			}
		}
	}
};
class frac{
public:
	bignum num,den;
	void reduce(){
		bignum u = num;
		bignum v = den;
		bignum k = 1;
		if(v == 0){
			k = v;
			u = 0;
			v = 1;
		}
		while(u != 0 && u != v){
			if(u.mod2() == 0){
				if(v.mod2() == 0){
					k.lshift();
					u.rshift();
					v.rshift();
				}else{
					u.rshift();
				}
			}else{
				if(v%2 == 0){
					v = v.rshift();
				}else{
					if(v > u){
						bignum oldu = u;
						u = (v-u);
						u.rshift();
						v = oldu;
					}else{
						u = (u-v);
						u.rshift();
					}
				}
			}
		}
		bignum GCD = k*v;
		num = num/GCD;
		den = den/GCD;
	}
	frac(bignum num,bignum den):num(num),den(den){
		reduce();
	}
	frac operator+=(frac b){
		if(den == b.den){
			num = num+b.num;
		}else{
			num = num*b.den + b.num*den;
			den = den * b.den;
		}
		reduce();
		return *this;
	}
	frac operator/(int b){
		frac n(num,b);
		n.reduce();
		n.den = n.den * den;
		return n;
	}
};*/
int main (int argc, char * const argv[]) {
	std::ifstream input("input.txt",std::ios::in);
	std::ofstream output("output.txt",std::ios::out);
	/*std::vector<std::vector<double> > weights;
	std::vector<double> avgTime;
	weights.push_back(std::vector<double>(1,1.0));
	weights.push_back(std::vector<double>(2,1.0));
	avgTime.push_back(0.0);
	avgTime.push_back(0.0);
	weights[1][0] = 0.0;
	for(int i = 2;i <= 1000;i++){
		std::vector<double> weight(i+1,0.0);
		for(int j = 0;j < i-1;j++){
			for(int k = 0;k <= j;k++){
				weight[k] += weights[j][k]/i;
			}
		}
		for(int k = 0;k <= i-1;k++){
			weight[k+1] += weights[i-1][k]/i;
		}
		double avg = 0;
		for(int q = 1;q <= i;q++){
			avg += weight[q]*avgTime[i-	q];
		}
		avg /= (1-weight[0]);
		double recip = 1/weight[0]; //Weight on self.
		avg = avg + 1/(recip-1) + 1;
		avgTime.push_back(avg);
		output << avg << "\n\n";
		weights.push_back(weight);
	}*/
	int T;
	input >> T;
	for(int i = 1; i <= T;i++){
		int N;
		input >> N;
		int wrong = 0;
		for(int j = 1;j <= N;j++){
			int x;
			input >> x;
			if(x != j) wrong++;
		}
		output << "Case #" << i << ": " << wrong << "\n";
	}
	output.flush();
	output.close();
    return 0;
}
