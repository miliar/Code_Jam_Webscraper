#include<cstdio>
#include<cctype>
#include<vector>
#include<map>

using namespace std;

struct PointerWithSum {
	unsigned long pointer;
	unsigned long sum;
};

PointerWithSum findNextPointer(unsigned long &currentPointer, unsigned long capacity, vector<unsigned long> &groupSizes);
bool solve(map<unsigned long, unsigned long> &pointerSum, vector<unsigned long> &pointers,
		   PointerWithSum pws, unsigned long long &profit, unsigned long rides, unsigned long ridesMadeSoFar);

class Input {
	static const int BUFSIZE = 1<<24;
	static char buffer[];
	char *bufpos;
	char *bufend;
	void grabBuffer();
public:
	Input() { grabBuffer(); }
	bool eof() { return bufend==buffer; }
	char nextChar() { return *bufpos; }
	inline char readChar();
	inline void skipWS();
	unsigned readUnsigned();
	unsigned long readUnsignedLong();
	int readInt();
	void readString(char *str);
};

char Input::buffer[Input::BUFSIZE];
void Input::grabBuffer() {
	bufpos = buffer;
	bufend = buffer + fread(buffer, 1, BUFSIZE, stdin);
}

char Input::readChar() {
	char res = *bufpos++;
	if(bufpos==bufend) grabBuffer();
	return res;
}

inline bool myisspace(char c) { return c<=' '; }

void Input::skipWS() {
	while(!eof() && myisspace(nextChar())) readChar();
}

unsigned long Input::readUnsignedLong() {
	skipWS();
	unsigned long res = 0;
	while(!eof() && isdigit(nextChar())) {
		res = 10u * res + (readChar() - '0');
	}
	return res;
}


int main() {
	freopen("input.txt","r",stdin);
	unsigned long i = 1;
	unsigned noOfTestCases;
	
	Input input;
	noOfTestCases = input.readUnsignedLong();
	while(i <= noOfTestCases) {
		unsigned long long profit = 0;
		unsigned long rides = input.readUnsignedLong();
		unsigned long capacity = input.readUnsignedLong();
		unsigned long groupCount = input.readUnsignedLong();
		vector<unsigned long> groupSizes;
		for(unsigned long j = 0; j < groupCount; j++) {
			unsigned long groupSize = input.readUnsignedLong();
			groupSizes.push_back(groupSize);
		}
		
		unsigned long currentPointer = 0;
		map <unsigned long, unsigned long> pointerSum;
		vector<unsigned long> pointers;
		for(unsigned long ridesMadeSoFar = 0; ridesMadeSoFar < rides; ridesMadeSoFar++) {
			//find the next pointer
			PointerWithSum pws = findNextPointer(currentPointer, capacity, groupSizes);
			//insert into hash table, and the vector of pointers if necessary, check if there's a cycle and handle it
			//also increment profit and return
			if(solve(pointerSum, pointers, pws, profit, rides, ridesMadeSoFar))
				break;
		}
		printf("Case #%lu: %llu\n", i, profit);
		i++;
	}
	
	return 0;
}

PointerWithSum findNextPointer(unsigned long &currentPointer, unsigned long capacity, vector<unsigned long> &groupSizes) {
	PointerWithSum pws;
	pws.sum = 0;
	pws.pointer = currentPointer;
	
	unsigned long currentPointerStart = currentPointer;
	
	while(true) {
		if(pws.sum + groupSizes[currentPointer] > capacity)
			break;
		pws.sum += groupSizes[currentPointer];
		currentPointer = (currentPointer + 1) % groupSizes.size();
		if(currentPointer == currentPointerStart)
			break;
	}
	
	//printf("%lu %lu\n", pws.pointer, pws.sum);
	return pws;
}

bool solve(map<unsigned long, unsigned long> &pointerSum, vector<unsigned long> &pointers,
		   PointerWithSum pws, unsigned long long &profit, unsigned long rides, unsigned long ridesMadeSoFar) {
	bool brk = false;
	
	if(pointerSum.insert(pair<unsigned long, unsigned long>(pws.pointer, pws.sum)).second == false) {
		//cycle found, based on remaining rides, change profit and return true
		//linear search for the pws.pointer
		unsigned long i = 0;
		
		for(; i < pointers.size(); i++) {
			if(pointers[i] == pws.pointer)
				break;
		}
		
		unsigned long cycleSize = pointers.size() - i;
		unsigned long ridesRemaining = rides - ridesMadeSoFar;
		unsigned long cycles = ridesRemaining / cycleSize;
		unsigned long lastRideCount = ridesRemaining % cycleSize;
		unsigned long long cycleSum = 0;
		unsigned long long lastRideSum = 0;
		
		for(unsigned long j = 0; i < pointers.size(); i++, j++) {
			if(j < lastRideCount)
				lastRideSum += pointerSum[pointers[i]];
			cycleSum += pointerSum[pointers[i]];
		}
		profit += cycles * cycleSum + lastRideSum;
		brk = true;
	}
	
	else {
		//add it to pointers vector, and increment profit
		pointers.push_back(pws.pointer);
		profit += pws.sum;
	}
	
	return brk;
}
