#include "m_combinations.h"

using namespace std;

combination::combination() {

}

combination::combination(char c1, char c2, char result, bool destroy) {
	this->c1 = c1;
	this->c2 = c2;
	this->result = result;
	this->destroy = destroy;
}

bool
combination::matches(char a, char b) {
	return ( ((a == c1) && (b == c2)) || ((a == c2) && (b == c1)));
}

bool
combination::is_destructive() {
	return destroy;
}	

char
combination::get_result() {
	return result;
}	

string
combination::to_string() {
	string ret = "";
	ret.push_back(c1);
	ret.append(" + ");
	ret.push_back(c2);
	ret.append(" = ");
	if (destroy) {
		ret.append("ZAP!");
	} else {
		ret.push_back(result);
	}

	return ret;
}

