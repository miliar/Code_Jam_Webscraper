#include <string>
#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
typedef unsigned long long ull;

struct Food {
	ull price, time;
	bool operator<(const Food &other) const {
		return price < other.price;
	}
};

struct Foods {
public:
	Foods(ull deliveryPrice, const std::vector<Food> &food): deliveryPrice(deliveryPrice), items(food) {
		std::sort(items.begin(), items.end());
	}
	ull costSingleDelivery(ull days) {
		if (days==0) return 0;
		ull totalItems = 0;
		ull totalCost = deliveryPrice;
		for (size_t i=0; i<items.size(); i++) {
			if (items[i].time<totalItems)
				continue;
			ull newItems = items[i].time - totalItems + 1;
			if (totalItems + newItems > days)
				newItems = days - totalItems;
			ull newCost = newItems * items[i].price;
			if (newCost/items[i].price != newItems)
				return inf;
			totalCost += newCost;
			if (totalCost<newCost)
				return inf;
			totalItems += newItems;
			if (totalItems==days)
				return totalCost;
		}
		return inf;
	}
	ull totalCost(ull days, ull numDeliveries) {
		if (numDeliveries>days) numDeliveries = days;
		ull smallDeliverySize = days / numDeliveries;
		ull largeDeliverySize = smallDeliverySize + 1;
		ull largeDeliveryCount = days - smallDeliverySize * numDeliveries;
		ull smallDeliveryCount = numDeliveries - largeDeliveryCount;
		ull smallCost = costSingleDelivery(smallDeliverySize);
		if (smallCost == inf) return inf;
		ull largeCost = costSingleDelivery(largeDeliverySize);
		if (largeDeliveryCount==0)
			largeCost = 1;
		if (largeCost == inf) return inf;
		ull totalSmallCost = smallCost * smallDeliveryCount;
		if (totalSmallCost / smallCost != smallDeliveryCount)
			return inf;
		ull totalLargeCost = largeCost * largeDeliveryCount;
		if (totalLargeCost / largeCost != largeDeliveryCount)
			return inf;
		ull sum = totalSmallCost + totalLargeCost;
		return sum<totalSmallCost ? inf : sum;
	}

	struct Res {
		ull cost;
		ull numDeliveries;
	};

	Res minCost(ull days, ull minDeliveries, ull maxDeliveries) {
		ull left = minDeliveries;
		ull right = maxDeliveries;
		ull costLeft = totalCost(days, left);
		ull costRight = totalCost(days, right);
		while (left!=right) {
			ull mid1 = left + (right-left)/2;
			ull mid2 = mid1 + 1;
			ull cost1 = totalCost(days, mid1);
			ull cost2 = totalCost(days, mid2);
			if (cost1<cost2 || (cost1==cost2 && costLeft<costRight))
				right = mid1;
			else
				left = mid2;
		}
		Res res;
		res.numDeliveries = left;
		res.cost = totalCost(days, left);
		return res;
	}

	Res minCost(ull days, ull numDeliveriesGuess) {
		ull cost = totalCost(days, numDeliveriesGuess);
		bool up = cost>totalCost(days, numDeliveriesGuess+1);
		ull step = 1;
		ull guess = numDeliveriesGuess;
		for (;;) {
			ull newGuess;
			if (up) {
				newGuess = guess + step;
			} else {
				if (guess>step) newGuess = guess - step;
				else return minCost(days, 1, guess);
			}
			ull newCost = totalCost(days, newGuess);
			if (newCost==inf || newCost>cost) {
				if (newGuess<numDeliveriesGuess)
					std::swap(numDeliveriesGuess, newGuess);
				return minCost(days, numDeliveriesGuess, newGuess);
			}
			guess = newGuess;
			step *= 2;
		}
	}

	ull maxDays(ull money) {
		ull days = 1;
		Res res = minCost(days, 1);
		if (res.cost>money) return 0;
		for (;;) {
			Res newRes = minCost(2*days, 2*res.numDeliveries);
			res = newRes;
			days *= 2;
			if (newRes.cost>money)
				break;
		}
		ull max = days;
		ull min = days/2;
		while (max!=min) {
			ull mid = (max+min+1)/2;
			if (minCost(mid, res.numDeliveries).cost>money)
				max = mid-1;
			else
				min = mid;
		}
		return max;
	}

	ull maxDays2(ull money) {
		for (ull days=1; ; days++) {
			bool ok = false;
			for (ull deliveries=1; deliveries<=days; deliveries++) {
				ull cost =  totalCost(days, deliveries);
				if (cost<=money) {
					ok = true;
					break;
				}
			}
			if (!ok)
				return days-1;
		}
	}

private:
	ull deliveryPrice;
	std::vector<Food> items;
	static const ull inf = static_cast<ull>(-1);
};

int main(int argc, const char **argv) {
	try {
		std::string inFilename(argc<=1 ? "in" : argv[1]);
		std::string outFilename = inFilename + ".out";
		std::ifstream fi(inFilename);
		fi.exceptions(std::ios::badbit | std::ios::failbit);
		std::ofstream fo(outFilename);
		fo.exceptions(std::ios::badbit | std::ios::failbit);
		int T;
		fi >> T;
		for (int i=1; i<=T; i++) {
			ull M, F, N;
			fi >> M >> F >> N;
			std::vector<Food> food(N);
			for (ull j=0; j<N; j++)
				fi >> food[j].price >> food[j].time;
			Foods foods(F, food);
#if 0
			ull ans1 = foods.maxDays(M);
			if (M<10000) {
				ull ans2 = foods.maxDays2(M);
				std::cerr << i << std::endl;
				if (ans1!=ans2) {
					std::cerr << "oh fuck\n";
				}
			}
#endif
			fo << "Case #" << i << ": " << foods.maxDays(M) << std::endl;
		}
	} catch (const std::exception &ex) {
		std::cerr << "\nexception: " << ex.what() << std::endl;
	} catch (...) {
		std::cerr << "\nwhoops\n";
	}
	return 0;
}
