#include <iostream>
#include <boost/shared_ptr.hpp>

class snapper {
	public:
		snapper() :
			on(false) {
		}
		bool on;
		boost::shared_ptr<snapper> next;
};

int main() {

	unsigned int T;
	std::cin >> T;

	for (unsigned int i = 0; i < T; ++i) {
		std::cout << "Case #"<<i+1<<": ";

		unsigned int N, K;
		std::cin >> N >> K;

		snapper* top = new snapper;
		snapper* cur = top;
		--N;
		while (N > 0) {
			cur->next = boost::shared_ptr<snapper>(new snapper);
			cur = (cur->next.get());
			--N;
		}

		while (K > 0) {
			cur = top;
			while (cur) {
				if (cur->on) {
					cur->on = false;
					cur = cur->next.get();
				} else {
					cur->on = true;
					break;
				}
			}
			--K;
		}

		cur = top;
		while (cur->next.get() && cur->on)
			cur = cur->next.get();

		if (!cur->next.get() && cur->on)
			std::cout << "ON";
		else
			std::cout << "OFF";

		delete top;

		std::cout << std::endl;
	}

}
