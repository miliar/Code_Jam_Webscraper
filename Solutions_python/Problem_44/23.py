def calculate_position(position, velocity, time):
    return position + velocity * time

def main():
    for case in range(input()):
        px = []
        py = []
        pz = []
        vx = []
        vy = []
        vz = []
        firefly_count = input()
        for n in range(firefly_count):
            params = list(map(int, raw_input().split()))
            px.append(params[0])
            py.append(params[1])
            pz.append(params[2])
            vx.append(params[3])
            vy.append(params[4])
            vz.append(params[5])
        px_sum = sum(px)
        py_sum = sum(py)
        pz_sum = sum(pz)
        vx_sum = sum(vx)
        vy_sum = sum(vy)
        vz_sum = sum(vz)
        if -0.0000000001 < vx_sum ** 2 + vy_sum ** 2 + vz_sum ** 2 < 0.0000000001:
            t = 0.0
        else:
            t = (-1.0) * (px_sum * vx_sum + py_sum * vy_sum + pz_sum * vz_sum) / (vx_sum ** 2 + vy_sum ** 2 + vz_sum ** 2)
        if t < 0.0:
            t = 0.0
        tpx_sum = sum(map(calculate_position, px, vx, [t for i in range(firefly_count)]))
        tpy_sum = sum(map(calculate_position, py, vy, [t for i in range(firefly_count)]))
        tpz_sum = sum(map(calculate_position, pz, vz, [t for i in range(firefly_count)]))
        d = ((tpx_sum ** 2 + tpy_sum ** 2 + tpz_sum ** 2) ** 0.5) / firefly_count
        print "Case #%d: %f %f" % (case + 1, d, t)
        
main()
