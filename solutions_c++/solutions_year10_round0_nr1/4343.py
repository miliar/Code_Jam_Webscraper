#ifndef SNAPPER_H
#define SNAPPER_H

class Snapper{
public:
	Snapper();
	bool powerin;
	bool onoroff;
	Snapper * next;
	void toggle();
};






#endif