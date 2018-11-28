#include <iostream>
#include <fstream>
#include <vector>

using std::shared_ptr;

struct Node {
	shared_ptr<Node> next;

	virtual void snap(bool has_power, bool had_power) = 0;
};

struct Snapper : Node {
	bool enabled;

	void snap(bool has_power, bool had_power) {
		if (had_power) {
			enabled = !enabled;
		}

		if (next) {
			next->snap(has_power && enabled, had_power && !enabled);
		}
	}

	Snapper() : enabled(false) { }
};

struct Lamp : Node {
	bool on;

	void snap(bool has_power, bool had_power) {
		on = has_power;
	}

	Lamp() : on(false) { }
};

int main() {
	const char *filename = "e:\\temp\\A-small-attempt0.in";
	std::ifstream file(filename);

	int count;
	file >> count;

	for (int i = 0; i < count; ++i) {
		int n, k;
		file >> n >> k;

		auto lamp = shared_ptr<Lamp>(new Lamp);
		shared_ptr<Node> prev_snapper = lamp;

		for (int j = 0; j < n; ++j) {
			auto snapper = shared_ptr<Snapper>(new Snapper);
			snapper->next = prev_snapper;
			prev_snapper = snapper;
		}

		for (int j = 0; j < k; ++j) {
			prev_snapper->snap(true, true);
		}

		std::cout << "Case #" << (i+1) << ": " << ((lamp->on) ? "ON" : "OFF") << "\n";
	}
}