#include <iostream>
#include <fstream>
#include <sysexits.h>
#include <string>

void flushline(std::istream &in)
{
	std::string tmp;
	std::getline(in, tmp);
}

unsigned CountToSwitchOn(unsigned n)
{
	static const unsigned cache_size = 35;
	static unsigned cache[cache_size];
	if (n > 1)
	{
		if (n < cache_size && cache[n]) return cache[n];
		return cache[n] = CountToSwitchOn(n - 1) * 2 + 1 /* CountToSwitchOff */;
	}
	return 1;
}

int main(int argc, char **argv)
{
	if (argc < 3)
	{
		std::cerr << "USAGE: " << argv[0] << " <file.in> <file.out>" << std::endl;
		return EX_USAGE;
	}
	const char *infname = argv[1];
	const char *outfname = argv[2];

	std::ifstream in(infname);
	if (!in.good())
	{
		std::cerr << "Unable to open file " << infname << " for reading" << std::endl;
		return EX_IOERR;
	}

	std::ofstream out(outfname);
	if (!out.good())
	{
		std::cerr << "Unable to open file " << outfname << " for writing" << std::endl;
		return EX_IOERR;
	}

	unsigned T = 0;
	in >> T;
	for (unsigned t = 1; t <= T; ++t)
	{
		unsigned N = 0, K = 0;
		in >> N >> K;
		unsigned cnt = CountToSwitchOn(N);
		bool isOn = false;
		//if (K >= cnt) isOn = (K + 1) % (cnt + 1) == 0;
		if (K >= cnt) isOn = (K - cnt) % (cnt + 1) == 0;
		out << "Case #" << t << ": " << (isOn ? "ON" : "OFF") << std::endl;
	}

	if (!in.good())
	{
		std::cerr << "Reading error" << std::endl;
		return EX_DATAERR;
	}
	flushline(in);
	flushline(in);
	if (!in.eof())
	{
		std::cerr << "Reading error(2)" << std::endl;
		return EX_DATAERR;
	}

	return EX_OK;
}
