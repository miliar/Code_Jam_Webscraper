#include<cstdio>
#include<cctype>


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
		unsigned long n = input.readUnsignedLong();
		unsigned long k = input.readUnsignedLong();
		n = (1 << n) - 1;
		if(k < n)
			printf("Case #%d: OFF\n", i);
		else
			printf("Case #%d: %s\n", i, ((k - n) % (n + 1) == 0)? "ON":"OFF");
		i++;
	}
	
	return 0;
}
